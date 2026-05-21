"""ArchiTinder Theme & Typography Explorer (port 5000).

Compares the 4 color themes × 2 fonts on 4 canonical screens.
The candidate sets live in `catalog.py` — edit there to add/remove options.

Run:
    python app.py
Open:
    http://127.0.0.1:5000/
"""
from __future__ import annotations

from dataclasses import asdict

from flask import Flask, jsonify, render_template

from catalog import FONTS, SCREENS, THEMES, TYPOGRAPHY_SCALE


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        themes=[asdict(t) for t in THEMES],
        fonts=[asdict(f) for f in FONTS],
        typography=TYPOGRAPHY_SCALE,
        screens=SCREENS,
    )


@app.route("/api/themes")
def api_themes():
    return jsonify({
        "themes": [asdict(t) for t in THEMES],
        "fonts": [asdict(f) for f in FONTS],
        "typography": TYPOGRAPHY_SCALE,
        "screens": SCREENS,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
