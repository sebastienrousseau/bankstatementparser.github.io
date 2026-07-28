#!/usr/bin/env python3
"""Verify every pacs008.com colour pair meets WCAG 2.1 AAA (>= 7:1).

Run: python3 audit/contrast.py
Exits non-zero if any text/UI pair falls below 7:1.
"""


def _lin(c: float) -> float:
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(fg: str, bg: str) -> float:
    la, lb = _luminance(fg), _luminance(bg)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


PAIRS = [
    # (label, foreground, background)
    ("light body text",     "#14181f", "#ffffff"),
    ("light muted / bg",    "#41474f", "#ffffff"),
    ("light muted / surf",  "#41474f", "#eef2f6"),
    ("light brand / bg",    "#1c4e9e", "#ffffff"),
    ("light brand / surf",  "#1c4e9e", "#eef2f6"),
    ("light btn text",      "#ffffff", "#173f86"),
    ("dark body text",      "#e8eef4", "#0d1117"),
    ("dark muted / bg",     "#aeb9c5", "#0d1117"),
    ("dark muted / surf",   "#aeb9c5", "#161c26"),
    ("dark brand / bg",     "#82b4ff", "#0d1117"),
    ("dark brand / surf",   "#82b4ff", "#161c26"),
    ("dark btn text",       "#0d1117", "#82b4ff"),
]

AAA = 7.0


def main() -> int:
    worst = 99.0
    print(f"{'pair':22} {'fg':9} {'bg':9} ratio  AAA(>=7)")
    for label, fg, bg in PAIRS:
        r = ratio(fg, bg)
        worst = min(worst, r)
        print(f"{label:22} {fg:9} {bg:9} {r:5.2f}  {'PASS' if r >= AAA else 'FAIL'}")
    print(f"\nworst pair: {worst:.2f}:1  ->  {'ALL AAA' if worst >= AAA else 'BELOW AAA'}")
    return 0 if worst >= AAA else 1


if __name__ == "__main__":
    raise SystemExit(main())
