"""ArchiTinder · Live design.md Preview.

Reads `design.md` next to this script, extracts the design tokens from its
```yaml fenced blocks, and renders the 4 canonical app screens with those
tokens applied. The browser polls `/api/mtime` once a second so any save to
`design.md` triggers an automatic page reload.

Run:
    python design_preview.py
Open:
    http://127.0.0.1:5001/

This server is independent of `app.py` (port 5000); both can run together.
"""
from __future__ import annotations

import re
from dataclasses import asdict
from pathlib import Path

from flask import Flask, jsonify, render_template

from catalog import FONTS, SCREENS, THEMES


HERE = Path(__file__).parent
DESIGN_MD = HERE / "design.md"


# ---------------------------------------------------------------------------
# Defaults — used when design.md is missing keys
# ---------------------------------------------------------------------------

DEFAULT_TOKENS: dict[str, str] = {
    # color
    "bg": "#0D1117", "surface": "#161B22",
    "surface-2": "#1F242C", "surface-3": "#30363D",
    "text": "#C9D1D9", "text-2": "#E6EDF3",
    "text-muted": "#8B949E", "text-dim": "#6E7681",
    "accent-1": "#58A6FF", "accent-2": "#7EE787", "accent-3": "#FFA657",
    "border": "rgba(255,255,255,0.1)",
    "border-soft": "rgba(255,255,255,0.14)",
    # typography
    "font-family": "IBM Plex Sans KR",
    "font-stack": '"IBM Plex Sans KR", -apple-system, BlinkMacSystemFont, system-ui, sans-serif',
    "h1-size": "48", "h1-weight": "700",
    "h2-size": "30", "h2-weight": "600",
    "body-size": "18", "body-weight": "400",
    "caption-size": "14", "caption-weight": "500",
    # layout
    "radius-card": "20",
    "radius-button": "12",
    "radius-pill": "999",
    "touch-target": "44",
    "tabbar-height": "64",
}


# ---------------------------------------------------------------------------
# Parser — extract simple `key: value` pairs from ```yaml fenced blocks
# ---------------------------------------------------------------------------

YAML_BLOCK = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL)
KV_LINE = re.compile(r'^([\w-]+)\s*:\s*(.+?)\s*$')


def parse_tokens(text: str) -> dict[str, str]:
    """Find every ```yaml block, extract key: value lines.

    Strips inline `# comment` from values (preserving hex codes like `#FFFFFF`
    by only treating `# ` after whitespace as a comment delimiter).
    """
    tokens: dict[str, str] = {}
    for block in YAML_BLOCK.findall(text):
        for raw in block.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = KV_LINE.match(line)
            if not m:
                continue
            key, val = m.group(1), m.group(2).strip()
            # Strip inline YAML comment ("  # ..." at end of value)
            # `\s+#` ensures we don't truncate hex values like "#FFFFFF".
            val = re.split(r"\s+#", val, maxsplit=1)[0].strip()
            # Strip wrapping quotes (single or double) if balanced
            if len(val) >= 2 and val[0] in ('"', "'") and val[-1] == val[0]:
                val = val[1:-1]
            tokens[key] = val
    return tokens


def load_design() -> dict:
    if not DESIGN_MD.exists():
        return {"tokens": DEFAULT_TOKENS, "mtime": 0, "source": ""}
    text = DESIGN_MD.read_text(encoding="utf-8")
    parsed = parse_tokens(text)
    # Merge with defaults so missing keys don't break the template.
    merged = {**DEFAULT_TOKENS, **parsed}
    return {
        "tokens": merged,
        "parsed_keys": list(parsed.keys()),
        "mtime": DESIGN_MD.stat().st_mtime,
        "source": text,
    }


# ---------------------------------------------------------------------------
# Flask app
# ---------------------------------------------------------------------------

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "design_preview.html",
        design=load_design(),
        screens=SCREENS,
        themes=[asdict(t) for t in THEMES],
        fonts=[asdict(f) for f in FONTS],
    )


@app.route("/api/mtime")
def mtime():
    return jsonify({
        "mtime": DESIGN_MD.stat().st_mtime if DESIGN_MD.exists() else 0,
    })


@app.route("/api/design")
def api_design():
    return jsonify({
        **load_design(),
        "themes": [asdict(t) for t in THEMES],
        "fonts": [asdict(f) for f in FONTS],
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
