from __future__ import annotations

import csv
import json
import re
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

import fitz
from docx import Document


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "source-documents"
OUT = Path(__file__).resolve().parents[1]
TEXT_DIR = OUT / "source_text"
CHUNK_DIR = OUT / "chunks"
REPORT_DIR = OUT / "reports"
OCR_TMP = OUT / "_ocr_tmp"

TIMESTAMP_RE = re.compile(
    r"^\s*(?:\d+\s+)?\d{2}:\d{2}:\d{2}[,.]\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}[,.]\d{3}.*$"
)


@dataclass
class SourceRecord:
    source_id: str
    file_name: str
    ext: str
    classification: str
    pages_or_slides: int | str
    size_mb: float
    extraction_method: str
    extraction_status: str
    text_chars: int
    chunks: int
    notes: str


def ensure_dirs() -> None:
    for d in (OUT, TEXT_DIR, CHUNK_DIR, REPORT_DIR, OCR_TMP):
        d.mkdir(parents=True, exist_ok=True)


def slugify(name: str) -> str:
    stem = Path(name).stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "_", stem).strip("_")
    return stem[:90] or "source"


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\uf02b", "+")
    text = text.replace("\u2022", "-")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_transcript_text(text: str) -> str:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.lower().startswith("file:///"):
            continue
        if TIMESTAMP_RE.match(line):
            continue
        if line.isdigit():
            continue
        if line.upper() == "[MUSIC]":
            continue
        lines.append(line)
    merged = " ".join(lines)
    merged = re.sub(r"\s+", " ", merged)
    return merged.strip()


def classify_pdf(path: Path, pages: int, direct_chars: int, meta_title: str = "") -> str:
    name = path.name.lower()
    title = meta_title.lower()
    if re.match(r"^[01]_[a-z0-9]+\.pdf$", name) or "transcripts" in title:
        return "video transcript"
    if "managerial-perspective" in name or "business-intelligence-analytics-and-data-science" in name:
        return "textbook"
    if "dashboard" in name:
        return "dashboard reading"
    if "governance" in name:
        return "data governance reading"
    if "warehousing" in name:
        return "data warehousing reading"
    if "aws" in name or "google cloud" in name:
        return "cloud analytics slides"
    if direct_chars < 500:
        return "image-only reading"
    return "reading"


def fitz_page_text(page: fitz.Page) -> str:
    return page.get_text("text") or ""


def load_ocr():
    try:
        from rapidocr_onnxruntime import RapidOCR

        return RapidOCR()
    except Exception:
        return None


def ocr_page(page: fitz.Page, ocr, image_path: Path, scale: float = 1.0) -> str:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    pix.save(image_path)
    result, _ = ocr(str(image_path))
    try:
        image_path.unlink(missing_ok=True)
    except Exception:
        pass
    if not result:
        return ""
    return "\n".join(str(line[1]) for line in result if len(line) > 1 and str(line[1]).strip())


def extract_pdf(path: Path, source_id: str, ocr) -> tuple[str, SourceRecord]:
    doc = fitz.open(path)
    meta_title = (doc.metadata or {}).get("title") or ""
    direct_pages: list[str] = []
    direct_chars = 0
    text_pages = 0
    for i in range(doc.page_count):
        txt = fitz_page_text(doc.load_page(i))
        chars = len(re.sub(r"\s+", "", txt))
        direct_chars += chars
        if chars > 50:
            text_pages += 1
        direct_pages.append(txt)

    classification = classify_pdf(path, doc.page_count, direct_chars, meta_title)
    use_direct = text_pages >= max(1, int(doc.page_count * 0.50)) and direct_chars > 700
    method = "fitz-text"
    status = "complete"
    notes = ""

    pages_out: list[str] = []
    if use_direct:
        low_text_pages = [
            i
            for i, txt in enumerate(direct_pages)
            if len(re.sub(r"\s+", "", txt)) <= 50
        ]
        low_text_page_numbers = {i + 1 for i in low_text_pages}
        page_cache: dict[str, str] = {}
        checkpoint_path = TEXT_DIR / f"{source_id}.ocr_pages.json"
        if low_text_pages and ocr and classification != "video transcript":
            method = "hybrid-fitz-text-rapidocr"
            if checkpoint_path.exists():
                try:
                    page_cache = json.loads(checkpoint_path.read_text(encoding="utf-8"))
                except Exception:
                    page_cache = {}
        elif low_text_pages and classification != "video transcript":
            method = "fitz-text-partial"
            status = "partial"
            notes = f"{len(low_text_pages)} low-text pages were not OCRed because OCR was unavailable."

        for i, txt in enumerate(direct_pages, start=1):
            body = clean_transcript_text(txt) if classification == "video transcript" else clean_text(txt)
            if i in low_text_page_numbers and ocr and classification != "video transcript":
                page_key = str(i)
                if page_key in page_cache:
                    txt = page_cache[page_key]
                    print(f"OCR {path.name}: page {i}/{doc.page_count} cached", flush=True)
                else:
                    img_path = OCR_TMP / f"{source_id}_page_{i:04d}.png"
                    try:
                        txt = ocr_page(doc.load_page(i - 1), ocr, img_path)
                    except Exception as exc:
                        txt = f"[OCR ERROR page {i}: {type(exc).__name__}: {exc}]"
                        status = "partial"
                    page_cache[page_key] = txt
                    checkpoint_path.write_text(json.dumps(page_cache, indent=2, ensure_ascii=False), encoding="utf-8")
                    print(f"OCR {path.name}: page {i}/{doc.page_count}", flush=True)
                ocr_body = clean_text(txt)
                if body and ocr_body and ocr_body not in body:
                    body = f"{body}\n{ocr_body}"
                elif ocr_body:
                    body = ocr_body
            if body:
                pages_out.append(f"\n\n--- Page {i} ---\n{body}")
    else:
        if not ocr:
            method = "ocr-unavailable"
            status = "needs_ocr"
            notes = "No direct text and RapidOCR unavailable."
        else:
            method = "rapidocr"
            checkpoint_path = TEXT_DIR / f"{source_id}.ocr_pages.json"
            page_cache: dict[str, str] = {}
            if checkpoint_path.exists():
                try:
                    page_cache = json.loads(checkpoint_path.read_text(encoding="utf-8"))
                except Exception:
                    page_cache = {}
            for i in range(doc.page_count):
                page_key = str(i + 1)
                if page_key in page_cache:
                    txt = page_cache[page_key]
                    print(f"OCR {path.name}: page {i + 1}/{doc.page_count} cached", flush=True)
                else:
                    page = doc.load_page(i)
                    img_path = OCR_TMP / f"{source_id}_page_{i + 1:04d}.png"
                    try:
                        txt = ocr_page(page, ocr, img_path)
                    except Exception as exc:
                        txt = f"[OCR ERROR page {i + 1}: {type(exc).__name__}: {exc}]"
                        status = "partial"
                    page_cache[page_key] = txt
                    checkpoint_path.write_text(json.dumps(page_cache, indent=2, ensure_ascii=False), encoding="utf-8")
                body = clean_text(txt)
                if body:
                    pages_out.append(f"\n\n--- Page {i + 1} ---\n{body}")
                print(f"OCR {path.name}: page {i + 1}/{doc.page_count}", flush=True)

    text = clean_text(f"# {path.name}\n\nClassification: {classification}\nExtraction: {method}\n" + "".join(pages_out))
    record = SourceRecord(
        source_id=source_id,
        file_name=path.name,
        ext=path.suffix.lower(),
        classification=classification,
        pages_or_slides=doc.page_count,
        size_mb=round(path.stat().st_size / 1024 / 1024, 2),
        extraction_method=method,
        extraction_status=status,
        text_chars=len(text),
        chunks=0,
        notes=notes,
    )
    return text, record


def pptx_text(path: Path) -> tuple[str, int]:
    ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    slides: list[tuple[int, str]] = []
    with zipfile.ZipFile(path) as z:
        names = [
            n
            for n in z.namelist()
            if re.match(r"ppt/slides/slide\d+\.xml$", n)
        ]
        names.sort(key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)))
        for name in names:
            idx = int(re.search(r"slide(\d+)\.xml", name).group(1))
            root = ET.fromstring(z.read(name))
            texts = [t.text or "" for t in root.findall(".//a:t", ns)]
            body = clean_text("\n".join(t for t in texts if t.strip()))
            slides.append((idx, body))
    rendered = [f"\n\n--- Slide {idx} ---\n{body}" for idx, body in slides if body]
    return clean_text(f"# {path.name}\n\nClassification: statistics/R slide deck\nExtraction: pptx-xml" + "".join(rendered)), len(names)


def docx_text(path: Path) -> tuple[str, int]:
    doc = Document(str(path))
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return clean_text(f"# {path.name}\n\nClassification: reference list\nExtraction: python-docx\n\n" + "\n\n".join(paras)), len(paras)


def chunk_text(text: str, source_id: str, max_chars: int = 6000, overlap: int = 700) -> list[dict]:
    text = clean_text(text)
    chunks: list[dict] = []
    start = 0
    idx = 1
    while start < len(text):
        end = min(len(text), start + max_chars)
        if end < len(text):
            boundary = max(text.rfind("\n\n", start, end), text.rfind(". ", start, end))
            if boundary > start + int(max_chars * 0.60):
                end = boundary + 1
        body = text[start:end].strip()
        if body:
            chunks.append({"source_id": source_id, "chunk_id": f"{source_id}_chunk_{idx:03d}", "text": body})
            idx += 1
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return chunks


def write_inventory(records: list[SourceRecord]) -> None:
    fields = list(SourceRecord.__dataclass_fields__.keys())
    with (REPORT_DIR / "source_inventory.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for rec in records:
            writer.writerow(rec.__dict__)
    with (REPORT_DIR / "source_inventory.json").open("w", encoding="utf-8") as f:
        json.dump([r.__dict__ for r in records], f, indent=2, ensure_ascii=False)

    lines = ["# Source Inventory\n"]
    lines.append("| Source | Type | Pages/Slides | Method | Status | Chunks | Notes |")
    lines.append("|---|---:|---:|---|---|---:|---|")
    for r in records:
        lines.append(
            f"| `{r.file_name}` | {r.classification} | {r.pages_or_slides} | {r.extraction_method} | {r.extraction_status} | {r.chunks} | {r.notes} |"
        )
    (REPORT_DIR / "source_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    start = time.time()
    ocr = load_ocr()
    records: list[SourceRecord] = []
    all_chunks: list[dict] = []
    files = sorted([p for p in SOURCE_ROOT.iterdir() if p.is_file() and p.suffix.lower() in {".pdf", ".pptx", ".docx"}], key=lambda p: p.name.lower())
    for path in files:
        source_id = slugify(path.name)
        print(f"Processing {path.name}", flush=True)
        if path.suffix.lower() == ".pdf":
            text, record = extract_pdf(path, source_id, ocr)
        elif path.suffix.lower() == ".pptx":
            text, count = pptx_text(path)
            record = SourceRecord(source_id, path.name, ".pptx", "statistics/R slide deck", count, round(path.stat().st_size / 1024 / 1024, 2), "pptx-xml", "complete", len(text), 0, "")
        elif path.suffix.lower() == ".docx":
            text, count = docx_text(path)
            record = SourceRecord(source_id, path.name, ".docx", "reference list", count, round(path.stat().st_size / 1024 / 1024, 2), "python-docx", "complete", len(text), 0, "")
        else:
            continue

        text_path = TEXT_DIR / f"{source_id}.md"
        text_path.write_text(text + "\n", encoding="utf-8")
        chunks = chunk_text(text, source_id)
        record.chunks = len(chunks)
        records.append(record)
        all_chunks.extend(chunks)
        with (CHUNK_DIR / f"{source_id}.jsonl").open("w", encoding="utf-8") as f:
            for chunk in chunks:
                f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    with (CHUNK_DIR / "all_chunks.jsonl").open("w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    write_inventory(records)
    elapsed = round(time.time() - start, 1)
    print(f"Done. Sources: {len(records)}. Chunks: {len(all_chunks)}. Seconds: {elapsed}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
