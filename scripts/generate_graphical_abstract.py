"""Generate the graphical abstract for the Preprints.org submission.

Preprints.org asks for a graphical abstract as a JPG or PNG, and explicitly
rejects a screenshot of the textual abstract. This draws the paper's core
claim instead: the five-element address that locates a knower against a
component under a declared binding.

Visual language matches the paper's figures: rounded rectangles, muted green
and amber fills, dark slate borders.

Usage:
    python scripts/generate_graphical_abstract.py

Output: preprint/graphical_abstract.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "preprint" / "graphical_abstract.png"

# Palette lifted from the existing print figures.
SLATE = "#22384a"
GREEN_FILL, GREEN_EDGE, GREEN_BADGE = "#e8f4ec", "#4a7c59", "#2d5a3d"
AMBER_FILL, AMBER_EDGE, AMBER_BADGE = "#fdf6e3", "#c9a227", "#a67c00"
WHITE_FILL = "#ffffff"
PANEL_FILL, PANEL_EDGE = "#f5f6f7", "#b8c0c7"
MUTED = "#5a6b78"

FONT = {"family": "DejaVu Sans"}


def box(ax, x, y, w, h, fill, edge, lw=1.6, r=0.045, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor=fill, edgecolor=edge, linewidth=lw, zorder=z))


def arrow(ax, x1, y1, x2, y2, color=SLATE, style="-", lw=1.8, z=3):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=15,
        linewidth=lw, color=color, linestyle=style,
        shrinkA=0, shrinkB=0, zorder=z))


fig, ax = plt.subplots(figsize=(10, 5.6), dpi=220)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.6)
ax.axis("off")
fig.patch.set_facecolor("white")

# ---------------------------------------------------------------- band 1
ax.text(0.25, 5.32, "THE PROBLEM", fontsize=8.5, color=MUTED,
        fontweight="bold", **FONT)

box(ax, 0.9, 4.28, 2.15, 0.82, WHITE_FILL, SLATE)
ax.text(1.975, 4.83, "Knower", ha="center", fontsize=11,
        fontweight="bold", color=SLATE, **FONT)
ax.text(1.975, 4.52, "person, role, team", ha="center", fontsize=8.5,
        color=MUTED, **FONT)

box(ax, 6.95, 4.28, 2.15, 0.82, WHITE_FILL, SLATE)
ax.text(8.025, 4.83, "Component", ha="center", fontsize=11,
        fontweight="bold", color=SLATE, **FONT)
ax.text(8.025, 4.52, "system part, tool", ha="center", fontsize=8.5,
        color=MUTED, **FONT)

ax.plot([3.15, 6.83], [4.69, 4.69], linestyle=(0, (5, 4)),
        color="#b04a4a", linewidth=1.8, zorder=2)
ax.text(4.99, 4.94, "?", ha="center", fontsize=15, fontweight="bold",
        color="#b04a4a", **FONT)
ax.text(4.99, 4.30, "the connection that is never recorded,\n"
                    "and disappears when people leave",
        ha="center", va="top", fontsize=8.5, color="#b04a4a", **FONT)

# ---------------------------------------------------------------- band 2
arrow(ax, 4.99, 3.98, 4.99, 3.66)

ax.text(0.25, 3.50, "THE ADDRESS", fontsize=8.5, color=MUTED,
        fontweight="bold", **FONT)

box(ax, 0.55, 1.70, 8.9, 1.62, PANEL_FILL, PANEL_EDGE, lw=1.2, r=0.06, z=1)

cells = [
    ("T1", "governing\nfield", AMBER_FILL, AMBER_EDGE),
    ("T2", "domain", AMBER_FILL, AMBER_EDGE),
    ("T3", "interface\nlayer", AMBER_FILL, AMBER_EDGE),
    ("C", "component\nanchor", GREEN_FILL, GREEN_EDGE),
    ("K", "knower\nanchor", GREEN_FILL, GREEN_EDGE),
]
cw, gap, y0 = 1.56, 0.20, 2.24
x = 0.86
for label, sub, fill, edge in cells:
    box(ax, x, y0, cw, 0.86, fill, edge)
    ax.text(x + cw / 2, y0 + 0.60, label, ha="center", fontsize=13,
            fontweight="bold", color=SLATE, **FONT)
    ax.text(x + cw / 2, y0 + 0.27, sub, ha="center", va="center",
            fontsize=8, color=MUTED, linespacing=1.25, **FONT)
    x += cw + gap

ax.plot([0.92, 5.08], [2.13, 2.13], color=AMBER_BADGE, linewidth=2.2, zorder=4)
ax.text(3.00, 1.87, "binding: fixes which layers are visible",
        ha="center", fontsize=8.5, color=AMBER_BADGE, **FONT)

ax.plot([6.96, 9.40], [2.13, 2.13], color=GREEN_BADGE, linewidth=2.2, zorder=4)
ax.text(8.18, 1.87, "anchors: let collections join",
        ha="center", fontsize=8.5, color=GREEN_BADGE, **FONT)

ax.text(4.99, 3.36, "two records name the same relation only when all five match",
        ha="center", va="top", fontsize=8.5, color=SLATE, style="italic", **FONT)

# ---------------------------------------------------------------- band 3
arrow(ax, 4.99, 1.62, 4.99, 1.32)

ax.text(0.25, 1.16, "WHAT IT PRODUCES", fontsize=8.5, color=MUTED,
        fontweight="bold", **FONT)

outs = [
    (0.55, "Verified record", "evidence attached,\nhuman-confirmed"),
    (3.72, "Comparable maps", "independent collections\ncan be differenced"),
    (6.89, "Loss made visible", "before it becomes\nunrecoverable"),
]
for bx, title, sub in outs:
    box(ax, bx, 0.20, 2.56, 0.86, GREEN_FILL, GREEN_EDGE)
    ax.text(bx + 1.28, 0.80, title, ha="center", fontsize=10.5,
            fontweight="bold", color=SLATE, **FONT)
    ax.text(bx + 1.28, 0.46, sub, ha="center", va="center", fontsize=8,
            color=MUTED, linespacing=1.25, **FONT)

fig.savefig(OUT, dpi=220, bbox_inches="tight", pad_inches=0.16,
            facecolor="white")
print(f"wrote {OUT}")

from PIL import Image  # noqa: E402
with Image.open(OUT) as im:
    if im.mode != "RGB":
        rgb = Image.new("RGB", im.size, (255, 255, 255))
        rgb.paste(im, mask=im.split()[-1] if im.mode == "RGBA" else None)
        rgb.save(OUT)
        im = rgb
    print(f"  {im.width} x {im.height} px, mode {im.mode}")
