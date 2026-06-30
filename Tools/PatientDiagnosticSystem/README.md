# Patient Diagnostic System

A terminal-styled diagnostic tool that assigns a random medical condition (or compliment) to any name you enter.

## Features

- 543 entries: medical conditions with severity levels 1–5, and positive compliments (prefixed with `x` in the source)
- Censor mode: replaces conditions with "BAD CONSEQUENCE"
- Colour-coded severity output
- Diagnostic history log

## Files

| File | Description |
|------|-------------|
| `illest.py` | Desktop app (Python + Tkinter) — run locally |
| `illnesses.txt` | Source data: 543 illnesses and compliments |

## Run locally

```bash
pip install tk
python illest.py
```

## Web version

Also available as an interactive tool on [eyosiyas.com/tools.html](https://eyosiyas.com/tools.html).