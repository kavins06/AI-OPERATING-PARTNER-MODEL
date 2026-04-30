# Codex Installation

This repo is meant to be the editable source of truth. Codex reads active skills from:

```text
C:\Users\kavin\.codex\skills
```

Use the install script to copy the repo version into the active Codex skills folder:

```powershell
.\scripts\install-codex-skills.ps1 -Force
```

The script copies every folder in `skills/` into the Codex skills folder. It also rewrites mastery-reference links in the installed copies so they point back to this repo's `mastery-reference/` folder.

Keep this repo under Git. Treat the installed Codex copies as deployed output.

