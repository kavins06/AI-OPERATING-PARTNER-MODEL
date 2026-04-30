#!/usr/bin/env python
"""Score risk severity from impact and likelihood values."""

from __future__ import annotations

import argparse
import csv
import sys


def label(score: int) -> str:
    if score >= 20:
        return "critical"
    if score >= 12:
        return "high"
    if score >= 6:
        return "medium"
    return "low"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--impact", type=int)
    parser.add_argument("--likelihood", type=int)
    parser.add_argument("--csv", help="CSV with impact_1_to_5 and likelihood_1_to_5 columns")
    args = parser.parse_args()

    if args.csv:
        with open(args.csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            writer = csv.DictWriter(sys.stdout, fieldnames=list(reader.fieldnames or []) + ["severity_score", "severity"])
            writer.writeheader()
            for row in reader:
                impact = int(row.get("impact_1_to_5") or 0)
                likelihood = int(row.get("likelihood_1_to_5") or 0)
                score = impact * likelihood
                row["severity_score"] = str(score)
                row["severity"] = label(score)
                writer.writerow(row)
        return 0

    if args.impact is None or args.likelihood is None:
        raise SystemExit("Provide --impact and --likelihood, or --csv")
    score = args.impact * args.likelihood
    print(f"Severity score: {score}")
    print(f"Severity: {label(score)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

