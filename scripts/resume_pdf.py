#!/usr/bin/env python3
"""Render a markdown resume to a clean, ATS-safe PDF.

Usage: python3 scripts/resume_pdf.py resume.md [resume.pdf]

Converts the markdown to styled HTML (python-markdown) and prints it to PDF
with headless Chromium. Requires: `pip install markdown` and a Chromium/Chrome
binary (CHROME_BIN env var, /opt/pw-browsers/chromium, or on PATH).
"""

import os
import shutil
import subprocess
import sys
import tempfile

import markdown

CSS = """
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 9.5pt; line-height: 1.3; color: #111;
  max-width: 7.6in; margin: 0 auto; padding: 0.45in 0.55in;
}
h1 { font-size: 16pt; margin: 0 0 2pt; text-align: center; letter-spacing: 1px; }
h1 + p, h1 + p + p { text-align: center; margin: 0 0 3pt; }
h1 + p { font-size: 10pt; color: #333; }
h2 {
  font-size: 10pt; text-transform: uppercase; letter-spacing: 1.5px;
  border-bottom: 1px solid #444; padding-bottom: 2pt; margin: 9pt 0 4pt;
}
h3 { font-size: 10pt; margin: 6pt 0 1pt; }
h3 + p { margin: 0 0 2pt; font-style: italic; color: #333; }
p { margin: 2.5pt 0; }
ul { margin: 2pt 0 5pt; padding-left: 15pt; }
li { margin: 1pt 0; }
a { color: #111; text-decoration: none; }
strong { font-weight: 600; }
"""

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head>
<body>{body}</body></html>"""


def find_chromium() -> str:
    candidates = [os.environ.get("CHROME_BIN"), "/opt/pw-browsers/chromium"]
    candidates += [shutil.which(n) for n in
                   ("chromium", "chromium-browser", "google-chrome", "chrome")]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    sys.exit("error: no Chromium/Chrome binary found (set CHROME_BIN)")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"

    with open(src, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(text, extensions=["smarty", "nl2br"])
    # PDF viewers show the HTML <title> as the document title; derive it from
    # the resume's name heading instead of the temp file's random name.
    name = next((ln.lstrip("# ").strip() for ln in text.splitlines()
                 if ln.startswith("# ")), "Resume")
    html = TEMPLATE.format(title=f"{name.title()} - Resume", css=CSS, body=body)

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(html)
        tmp_path = tmp.name
    try:
        subprocess.run(
            [find_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={out}",
             f"file://{tmp_path}"],
            check=True, capture_output=True, text=True)
    finally:
        os.unlink(tmp_path)
    print(out)


if __name__ == "__main__":
    main()
