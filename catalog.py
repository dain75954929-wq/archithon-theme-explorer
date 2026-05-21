"""Shared design catalog: themes · fonts · screens · type scale.

Both `app.py` (theme explorer at :5000) and `design_preview.py` (design.md
live preview at :5001) import from this module so the candidate sets stay in
sync. Edit here to add/remove candidates.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Font:
    id: str
    name: str
    stack: str
    category: Literal["sans-serif", "serif"]
    note: str


# Korean fallback chain: web font → OS-installed Korean → system-ui (design.md §2.1)
IBM_PLEX = (
    '"IBM Plex Sans KR", '
    '"Noto Sans KR", '            # web fallback (Google Fonts)
    '"Apple SD Gothic Neo", '     # macOS / iOS
    '"Malgun Gothic", "맑은 고딕", '  # Windows
    'system-ui, -apple-system, BlinkMacSystemFont, sans-serif'
)
NOTO_SERIF = (
    '"Noto Serif KR", "본명조", '
    '"Nanum Myeongjo", "나눔명조", '  # web/installed Korean serif
    '"AppleMyungjo", '             # macOS / iOS Korean serif
    '"Batang", "바탕", '            # Windows Korean serif
    'Georgia, serif'
)


FONTS: list[Font] = [
    Font("ibm-plex", "IBM Plex Sans KR", IBM_PLEX, "sans-serif",
         "IBM의 기업 폰트. 기하학적이고 테크니컬한 인상."),
    Font("noto-serif", "Noto Serif KR", NOTO_SERIF, "serif",
         "구글 노토 명조체. 고전적이고 차분한 분위기."),
]


# ---------------------------------------------------------------------------
# Color themes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Theme:
    id: str
    name: str
    mode: Literal["light", "dark"]
    bg: str
    surface: str
    surface2: str
    surface3: str
    text: str
    text2: str
    text_muted: str
    text_dim: str
    accent1: str
    accent2: str
    accent3: str
    recommended_font: str


THEMES: list[Theme] = [
    # ---- Light ----
    Theme("github-light", "GitHub Light", "light",
          bg="#FFFFFF", surface="#F6F8FA", surface2="#EFF2F5", surface3="#E1E4E8",
          text="#1F2328", text2="#24292F", text_muted="#656D76", text_dim="#8C959F",
          accent1="#0969DA", accent2="#8250DF", accent3="#953800",
          recommended_font="ibm-plex"),
    Theme("ayu-light", "Ayu Light", "light",
          bg="#FAFAFA", surface="#FFFFFF", surface2="#F0F0F0", surface3="#E0E0E0",
          text="#5C6773", text2="#3E4B59", text_muted="#ABB0B6", text_dim="#C0C5CB",
          accent1="#F29718", accent2="#F07178", accent3="#36A3D9",
          recommended_font="noto-serif"),

    # ---- Dark ----
    Theme("github-dark", "GitHub Dark", "dark",
          bg="#0D1117", surface="#161B22", surface2="#1F242C", surface3="#30363D",
          text="#C9D1D9", text2="#E6EDF3", text_muted="#8B949E", text_dim="#6E7681",
          accent1="#58A6FF", accent2="#7EE787", accent3="#FFA657",
          recommended_font="ibm-plex"),
    Theme("synthwave", "SynthWave '84", "dark",
          bg="#262335", surface="#34294F", surface2="#3D3057", surface3="#463B6A",
          text="#F4EEE4", text2="#FFFFFF", text_muted="#B6B1B1", text_dim="#807878",
          accent1="#FF7EDB", accent2="#FEF983", accent3="#36ADF1",
          recommended_font="noto-serif"),
]


# ---------------------------------------------------------------------------
# Type scale + screens
# ---------------------------------------------------------------------------

TYPOGRAPHY_SCALE = [
    {"name": "H1",      "size": 48, "weight": 700, "usage": "Main Title"},
    {"name": "H2",      "size": 30, "weight": 600, "usage": "Sub Title"},
    {"name": "Body",    "size": 18, "weight": 400, "usage": "Main Text"},
    {"name": "Caption", "size": 14, "weight": 500, "usage": "Tags / Meta"},
]


SCREENS = [
    {"id": "ai-search", "name": "AI Search", "nav": "search"},
    {"id": "discovery", "name": "Discovery", "nav": "discover"},
    {"id": "persona",   "name": "Persona",   "nav": "profile"},
    {"id": "boards",    "name": "Boards",    "nav": "boards"},
]
