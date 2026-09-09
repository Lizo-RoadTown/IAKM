from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape


ROOT_DIR = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT_DIR / "figures"
SVG_PATH = FIGURES_DIR / "figure_paper3_multilevel_collapsing_dsm_funnel.svg"

WIDTH = 1800
HEIGHT = 2920

PROPERTY_ORDER = ["Location", "Density", "Structure", "Degradation"]
PROPERTY_SHORT = {
    "Location": "Loc",
    "Density": "Den",
    "Structure": "Str",
    "Degradation": "Deg",
}
PROPERTY_COLORS = {
    "Location": "#2B6CB0",
    "Density": "#C48A1A",
    "Structure": "#0F8C7A",
    "Degradation": "#D65F4A",
}
TRADITION_COLORS = {
    "EP": "#315C8A",
    "SD": "#0F8C7A",
    "ITH": "#C48A1A",
    "CS": "#2B6CB0",
    "EVO": "#D65F4A",
    "KM": "#8B6B3F",
    "KLT": "#6F7D4C",
    "ISY": "#4C7EA8",
    "ISC": "#5D8395",
}

TRADITIONS = [
    {"code": "EP", "name": "Epistemology", "properties": {"Location"}},
    {
        "code": "SD",
        "name": "Situated / distributed cognition",
        "properties": {"Location", "Density", "Structure", "Degradation"},
    },
    {"code": "ITH", "name": "Information theory / entropy", "properties": {"Density", "Degradation"}},
    {"code": "CS", "name": "Complexity / systems science", "properties": {"Structure"}},
    {"code": "EVO", "name": "Evolutionary epistemology", "properties": {"Structure", "Degradation"}},
    {
        "code": "KM",
        "name": "Knowledge management",
        "properties": {"Density", "Structure", "Degradation"},
    },
    {"code": "KLT", "name": "Knowledge loss / turnover", "properties": {"Density", "Degradation"}},
    {"code": "ISY", "name": "Information systems", "properties": {"Structure", "Degradation"}},
    {"code": "ISC", "name": "Information science", "properties": {"Structure", "Degradation"}},
]

LEVEL1_INTERFACES = [
    ("EP", "SD", ["Location"], 2),
    ("SD", "ITH", ["Degradation"], 3),
    ("SD", "EVO", ["Degradation"], 2),
    ("SD", "KM", ["Degradation", "Density"], 3),
    ("SD", "CS", ["Structure"], 2),
    ("ITH", "EVO", ["Degradation"], 2),
    ("ITH", "KM", ["Degradation", "Density"], 3),
    ("ITH", "KLT", ["Degradation", "Density"], 2),
    ("CS", "EVO", ["Structure"], 2),
    ("CS", "ISY", ["Structure"], 2),
    ("CS", "ISC", ["Structure"], 2),
    ("EVO", "KM", ["Structure", "Degradation"], 3),
    ("KM", "KLT", ["Degradation", "Density"], 3),
    ("KM", "ISY", ["Structure", "Degradation"], 2),
    ("KM", "ISC", ["Structure", "Degradation"], 2),
    ("ISY", "ISC", ["Structure", "Degradation"], 2),
]

LEVEL2_BRIDGES = {
    ("Location", "Density"): ["SD"],
    ("Location", "Structure"): ["SD"],
    ("Location", "Degradation"): ["SD"],
    ("Density", "Structure"): ["SD", "KM"],
    ("Density", "Degradation"): ["SD", "ITH", "KM"],
    ("Structure", "Degradation"): ["SD", "EVO", "KM", "ISY", "ISC"],
}

LEVEL3_COUNTS = {
    ("Location", "Density"): 1,
    ("Location", "Structure"): 1,
    ("Location", "Degradation"): 1,
    ("Density", "Structure"): 2,
    ("Density", "Degradation"): 3,
    ("Structure", "Degradation"): 5,
}


def rgb_components(hex_color: str) -> tuple[int, int, int]:
    normalized = hex_color.lstrip("#")
    return tuple(int(normalized[index:index + 2], 16) for index in (0, 2, 4))


def blend(hex_a: str, hex_b: str, mix: float) -> str:
    red_a, green_a, blue_a = rgb_components(hex_a)
    red_b, green_b, blue_b = rgb_components(hex_b)
    red = round(red_a + (red_b - red_a) * mix)
    green = round(green_a + (green_b - green_a) * mix)
    blue = round(blue_a + (blue_b - blue_a) * mix)
    return f"#{red:02X}{green:02X}{blue:02X}"


def svg_text(x: float, y: float, text: str, class_name: str, anchor: str | None = None) -> str:
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" class="{class_name}"{anchor_attr}>{escape(text)}</text>'


def svg_rect(x: float, y: float, width: float, height: float, **attrs: str | float) -> str:
    attributes = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" {attributes}/>'


def svg_line(x1: float, y1: float, x2: float, y2: float, **attrs: str | float) -> str:
    attributes = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {attributes}/>'


def svg_circle(cx: float, cy: float, radius: float, **attrs: str | float) -> str:
    attributes = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{radius}" {attributes}/>'


def svg_path(path_data: str, **attrs: str | float) -> str:
    attributes = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<path d="{path_data}" {attributes}/>'


def chip(x: float, y: float, width: float, height: float, label: str, fill: str, stroke: str, text_fill: str, class_name: str = "chip-label") -> str:
    text_x = x + width / 2
    text_y = y + height / 2 + 4
    return "\n".join(
        [
            svg_rect(x, y, width, height, rx=height / 2, fill=fill, stroke=stroke, **{"stroke-width": 1.2}),
            f'<text x="{text_x}" y="{text_y}" class="{class_name}" text-anchor="middle" fill="{text_fill}">{escape(label)}</text>',
        ]
    )


def draw_panel_background(x: float, y: float, width: float, height: float) -> str:
    return "\n".join(
        [
            svg_rect(x + 18, y + 24, width, height, rx=24, fill="#D8E1EA", opacity="0.18"),
            svg_rect(x, y, width, height, rx=24, fill="#FFFFFF", stroke="#D5DEE7", **{"stroke-width": 1.4}),
        ]
    )


def level1_lookup() -> dict[tuple[str, str], tuple[list[str], int]]:
    lookup: dict[tuple[str, str], tuple[list[str], int]] = {}
    for left_code, right_code, properties, magnitude in LEVEL1_INTERFACES:
        lookup[(left_code, right_code)] = (properties, magnitude)
        lookup[(right_code, left_code)] = (properties, magnitude)
    return lookup


def level2_lookup() -> dict[tuple[str, str], list[str]]:
    lookup: dict[tuple[str, str], list[str]] = {}
    for key, values in LEVEL2_BRIDGES.items():
        left_property, right_property = key
        lookup[(left_property, right_property)] = values
        lookup[(right_property, left_property)] = values
    return lookup


def level3_lookup() -> dict[tuple[str, str], int]:
    lookup: dict[tuple[str, str], int] = {}
    for key, value in LEVEL3_COUNTS.items():
        left_property, right_property = key
        lookup[(left_property, right_property)] = value
        lookup[(right_property, left_property)] = value
    return lookup


def draw_level1() -> tuple[str, dict[str, float], dict[str, dict[str, tuple[float, float]]]]:
    fragments: list[str] = []
    panel_x = 105
    panel_y = 180
    panel_width = 1590
    panel_height = 845
    fragments.append(draw_panel_background(panel_x, panel_y, panel_width, panel_height))

    fragments.append(svg_text(112, 120, "Figure 2. Multi-level collapsing MDM of convergence structure", "title"))
    fragments.append(
        svg_text(
            112,
            152,
            "Level 1 shows tradition-level interfaces, Level 2 exposes which traditions bridge property clusters, and Level 3 reduces those bridges to coupling strength.",
            "subtitle",
        )
    )
    fragments.append(svg_text(135, 225, "Level 1: Tradition-level DSM (9 x 9)", "section-title"))
    fragments.append(
        svg_text(
            135,
            252,
            "Vector thickness encodes convergence magnitude (1-3). Right-margin badges show which properties each tradition reached.",
            "section-note",
        )
    )

    grid_x = 610
    grid_y = 315
    cell_size = 62
    grid_size = cell_size * len(TRADITIONS)
    label_x = 165
    badges_x = 1220
    badges_y = grid_y - 4
    row_centers: dict[str, float] = {}
    badge_centers: dict[str, dict[str, tuple[float, float]]] = {}
    code_to_index = {tradition["code"]: index for index, tradition in enumerate(TRADITIONS)}
    interface_lookup = level1_lookup()

    fragments.append(svg_text(label_x, grid_y - 48, "Tradition", "axis-label"))
    fragments.append(svg_text(grid_x, grid_y - 48, "Tradition-by-tradition interfaces", "axis-label"))
    fragments.append(svg_text(badges_x, grid_y - 48, "Properties reached", "axis-label"))

    for column_index, tradition in enumerate(TRADITIONS):
        x_position = grid_x + column_index * cell_size + cell_size / 2
        fragments.append(svg_text(x_position, grid_y - 18, tradition["code"], "column-label", "middle"))

    fragments.append(svg_rect(grid_x, grid_y, grid_size, grid_size, fill="#FCFDFE", stroke="#C8D4DF", **{"stroke-width": 1.2}))
    for grid_index in range(len(TRADITIONS) + 1):
        offset = grid_index * cell_size
        fragments.append(svg_line(grid_x + offset, grid_y, grid_x + offset, grid_y + grid_size, stroke="#D8E1EA", **{"stroke-width": 1}))
        fragments.append(svg_line(grid_x, grid_y + offset, grid_x + grid_size, grid_y + offset, stroke="#D8E1EA", **{"stroke-width": 1}))

    for diagonal_index in range(len(TRADITIONS)):
        diagonal_x = grid_x + diagonal_index * cell_size
        diagonal_y = grid_y + diagonal_index * cell_size
        fragments.append(svg_rect(diagonal_x, diagonal_y, cell_size, cell_size, fill="#EFF4F8", stroke="none"))

    for row_index, tradition in enumerate(TRADITIONS):
        row_center = grid_y + row_index * cell_size + cell_size / 2
        row_centers[tradition["code"]] = row_center
        fragments.append(svg_text(label_x, row_center + 5, tradition["name"], "row-label"))

        badge_centers[tradition["code"]] = {}
        for property_index, property_name in enumerate(PROPERTY_ORDER):
            badge_x = badges_x + property_index * 68
            badge_y = badges_y + row_index * cell_size
            filled = property_name in tradition["properties"]
            fill = PROPERTY_COLORS[property_name] if filled else "#EEF3F7"
            stroke = PROPERTY_COLORS[property_name] if filled else "#D7E0E8"
            text_fill = "#FFFFFF" if filled else "#5B6777"
            class_name = "chip-label" if filled else "chip-label-muted"
            fragments.append(chip(badge_x, badge_y + 19, 48, 24, PROPERTY_SHORT[property_name], fill, stroke, text_fill, class_name))
            badge_centers[tradition["code"]][property_name] = (badge_x + 24, badge_y + 31)

    stroke_widths = {1: 1.8, 2: 3.2, 3: 5.0}
    for row_index, row_tradition in enumerate(TRADITIONS):
        for column_index, column_tradition in enumerate(TRADITIONS):
            if row_index == column_index:
                continue
            interface = interface_lookup.get((row_tradition["code"], column_tradition["code"]))
            if not interface:
                continue
            properties, magnitude = interface
            cell_x = grid_x + column_index * cell_size
            cell_y = grid_y + row_index * cell_size
            if row_index < column_index:
                start_x = cell_x + 15
                start_y = cell_y + 46
                end_x = cell_x + 47
                end_y = cell_y + 14
            else:
                start_x = cell_x + 47
                start_y = cell_y + 14
                end_x = cell_x + 15
                end_y = cell_y + 46
            fragments.append(
                svg_line(
                    start_x,
                    start_y,
                    end_x,
                    end_y,
                    stroke="#334155",
                    **{
                        "stroke-width": stroke_widths[magnitude],
                        "stroke-linecap": "round",
                        "marker-end": "url(#arrow-head)",
                    },
                )
            )

            dot_span = len(properties) * 12
            dot_start_x = cell_x + (cell_size - dot_span) / 2 + 6
            for property_index, property_name in enumerate(properties):
                fragments.append(
                    svg_circle(
                        dot_start_x + property_index * 12,
                        cell_y + 53,
                        3.6,
                        fill=PROPERTY_COLORS[property_name],
                        stroke="#FFFFFF",
                        **{"stroke-width": 0.8},
                    )
                )

    legend_x = 1435
    legend_y = 318
    fragments.append(svg_text(legend_x, legend_y - 32, "Magnitude", "axis-label"))
    for magnitude in (1, 2, 3):
        entry_y = legend_y + (magnitude - 1) * 28
        fragments.append(
            svg_line(
                legend_x,
                entry_y,
                legend_x + 34,
                entry_y,
                stroke="#334155",
                **{
                    "stroke-width": stroke_widths[magnitude],
                    "stroke-linecap": "round",
                    "marker-end": "url(#arrow-head)",
                },
            )
        )
        fragments.append(svg_text(legend_x + 48, entry_y + 4, f"{magnitude}", "legend-text"))

    badge_legend_y = 442
    fragments.append(svg_text(legend_x, badge_legend_y - 22, "Badge colors", "axis-label"))
    for property_index, property_name in enumerate(PROPERTY_ORDER):
        legend_entry_y = badge_legend_y + property_index * 28
        fragments.append(svg_circle(legend_x + 8, legend_entry_y - 4, 6, fill=PROPERTY_COLORS[property_name], stroke="#FFFFFF", **{"stroke-width": 0.8}))
        fragments.append(svg_text(legend_x + 24, legend_entry_y, f"{PROPERTY_SHORT[property_name]} = {property_name}", "legend-text"))

    return "\n".join(fragments), row_centers, badge_centers


def draw_level2(row_centers: dict[str, float], badge_centers: dict[str, dict[str, tuple[float, float]]]) -> tuple[str, dict[str, tuple[float, float]]]:
    fragments: list[str] = []
    panel_x = 235
    panel_y = 1095
    panel_width = 1330
    panel_height = 855
    fragments.append(draw_panel_background(panel_x, panel_y, panel_width, panel_height))
    fragments.append(svg_text(265, 1141, "Level 2: Cluster-level DSM (4 x 4)", "section-title"))
    fragments.append(
        svg_text(
            265,
            1168,
            "Each off-diagonal cell lists the traditions that bridge those two property clusters. This is the new structure revealed by the collapse.",
            "section-note",
        )
    )

    grid_x = 745
    grid_y = 1265
    cell_size = 136
    grid_size = cell_size * len(PROPERTY_ORDER)
    property_centers: dict[str, tuple[float, float]] = {}
    bridge_lookup = level2_lookup()

    for property_index, property_name in enumerate(PROPERTY_ORDER):
        chip_x = grid_x + property_index * cell_size + 10
        chip_y = 1215
        fragments.append(
            chip(
                chip_x,
                chip_y,
                116,
                30,
                property_name,
                blend(PROPERTY_COLORS[property_name], "#FFFFFF", 0.84),
                PROPERTY_COLORS[property_name],
                PROPERTY_COLORS[property_name],
            )
        )
        property_centers[property_name] = (chip_x + 58, chip_y + 15)
        fragments.append(svg_text(350, grid_y + property_index * cell_size + cell_size / 2 + 5, property_name, "row-label"))

    fragments.append(svg_text(350, 1237, "Property cluster", "axis-label"))
    fragments.append(svg_rect(grid_x, grid_y, grid_size, grid_size, fill="#FCFDFE", stroke="#C8D4DF", **{"stroke-width": 1.2}))
    for grid_index in range(len(PROPERTY_ORDER) + 1):
        offset = grid_index * cell_size
        fragments.append(svg_line(grid_x + offset, grid_y, grid_x + offset, grid_y + grid_size, stroke="#D8E1EA", **{"stroke-width": 1}))
        fragments.append(svg_line(grid_x, grid_y + offset, grid_x + grid_size, grid_y + offset, stroke="#D8E1EA", **{"stroke-width": 1}))

    for diagonal_index in range(len(PROPERTY_ORDER)):
        diagonal_x = grid_x + diagonal_index * cell_size
        diagonal_y = grid_y + diagonal_index * cell_size
        fragments.append(svg_rect(diagonal_x, diagonal_y, cell_size, cell_size, fill="#EFF4F8", stroke="none"))
        fragments.append(svg_text(diagonal_x + cell_size / 2, diagonal_y + cell_size / 2 + 6, "-", "count-text", "middle"))

    for tradition in TRADITIONS:
        start_code = tradition["code"]
        for property_name in tradition["properties"]:
            start_x, start_y = badge_centers[start_code][property_name]
            end_x, end_y = property_centers[property_name]
            fragments.append(
                svg_path(
                    f"M {start_x} {start_y} C {start_x + 45} {start_y + 140}, {end_x - 34} {end_y - 95}, {end_x} {end_y}",
                    fill="none",
                    stroke=PROPERTY_COLORS[property_name],
                    **{"stroke-width": 1.6, "stroke-opacity": 0.23},
                )
            )

    for row_index, row_property in enumerate(PROPERTY_ORDER):
        for column_index, column_property in enumerate(PROPERTY_ORDER):
            if row_index == column_index:
                continue
            bridges = bridge_lookup.get((row_property, column_property), [])
            if not bridges:
                continue
            cell_x = grid_x + column_index * cell_size
            cell_y = grid_y + row_index * cell_size
            fill_mix = 0.93 if len(bridges) < 3 else 0.88
            fragments.append(
                svg_rect(
                    cell_x + 4,
                    cell_y + 4,
                    cell_size - 8,
                    cell_size - 8,
                    rx=14,
                    fill=blend(PROPERTY_COLORS[row_property], "#FFFFFF", fill_mix),
                    opacity="0.32",
                    stroke="none",
                )
            )
            pill_width = 42
            pill_height = 24
            columns = 3 if len(bridges) >= 4 else 2 if len(bridges) == 3 else len(bridges)
            rows = (len(bridges) + columns - 1) // columns
            total_width = columns * pill_width + (columns - 1) * 8
            total_height = rows * pill_height + (rows - 1) * 9
            start_x = cell_x + (cell_size - total_width) / 2
            start_y = cell_y + (cell_size - total_height) / 2
            for bridge_index, bridge_code in enumerate(bridges):
                row_offset = bridge_index // columns
                column_offset = bridge_index % columns
                pill_x = start_x + column_offset * (pill_width + 8)
                pill_y = start_y + row_offset * (pill_height + 9)
                fragments.append(
                    chip(
                        pill_x,
                        pill_y,
                        pill_width,
                        pill_height,
                        bridge_code,
                        blend(TRADITION_COLORS[bridge_code], "#FFFFFF", 0.84),
                        TRADITION_COLORS[bridge_code],
                        TRADITION_COLORS[bridge_code],
                        "mini-chip-label",
                    )
                )

    return "\n".join(fragments), property_centers


def draw_level3(property_centers: dict[str, tuple[float, float]]) -> str:
    fragments: list[str] = []
    panel_x = 355
    panel_y = 2015
    panel_width = 1090
    panel_height = 845
    fragments.append(draw_panel_background(panel_x, panel_y, panel_width, panel_height))
    fragments.append(svg_text(387, 2060, "Level 3: Property-level DSM (4 x 4)", "section-title"))
    fragments.append(
        svg_text(
            387,
            2087,
            "Bridging traditions are replaced by counts, revealing the convergence skeleton. Darker cells indicate stronger co-occurrence.",
            "section-note",
        )
    )

    grid_x = 760
    grid_y = 2180
    cell_size = 136
    grid_size = cell_size * len(PROPERTY_ORDER)
    count_lookup = level3_lookup()
    bottom_centers: dict[str, tuple[float, float]] = {}

    for property_index, property_name in enumerate(PROPERTY_ORDER):
        chip_x = grid_x + property_index * cell_size + 10
        chip_y = 2130
        fragments.append(
            chip(
                chip_x,
                chip_y,
                116,
                30,
                property_name,
                blend(PROPERTY_COLORS[property_name], "#FFFFFF", 0.84),
                PROPERTY_COLORS[property_name],
                PROPERTY_COLORS[property_name],
            )
        )
        bottom_centers[property_name] = (chip_x + 58, chip_y + 15)
        fragments.append(svg_text(440, grid_y + property_index * cell_size + cell_size / 2 + 5, property_name, "row-label"))

    fragments.append(svg_rect(grid_x, grid_y, grid_size, grid_size, fill="#FCFDFE", stroke="#C8D4DF", **{"stroke-width": 1.2}))
    for grid_index in range(len(PROPERTY_ORDER) + 1):
        offset = grid_index * cell_size
        fragments.append(svg_line(grid_x + offset, grid_y, grid_x + offset, grid_y + grid_size, stroke="#D8E1EA", **{"stroke-width": 1}))
        fragments.append(svg_line(grid_x, grid_y + offset, grid_x + grid_size, grid_y + offset, stroke="#D8E1EA", **{"stroke-width": 1}))

    for property_name, (start_x, start_y) in property_centers.items():
        end_x, end_y = bottom_centers[property_name]
        fragments.append(
            svg_path(
                f"M {start_x} {start_y} C {start_x} {start_y + 96}, {end_x} {end_y - 96}, {end_x} {end_y}",
                fill="none",
                stroke="#94A3B8",
                **{"stroke-width": 1.8, "stroke-opacity": 0.36},
            )
        )

    for row_index, row_property in enumerate(PROPERTY_ORDER):
        for column_index, column_property in enumerate(PROPERTY_ORDER):
            cell_x = grid_x + column_index * cell_size
            cell_y = grid_y + row_index * cell_size
            if row_index == column_index:
                fragments.append(svg_rect(cell_x + 4, cell_y + 4, cell_size - 8, cell_size - 8, rx=14, fill="#EFF4F8", stroke="none"))
                fragments.append(svg_text(cell_x + cell_size / 2, cell_y + cell_size / 2 + 6, "-", "count-text", "middle"))
                continue
            count = count_lookup[(row_property, column_property)]
            intensity = (count - 1) / 4
            fill = blend("#E8EFF5", "#44576C", intensity)
            text_fill = "#FFFFFF" if count >= 4 else "#1F2937"
            fragments.append(svg_rect(cell_x + 4, cell_y + 4, cell_size - 8, cell_size - 8, rx=14, fill=fill, stroke="none"))
            fragments.append(
                f'<text x="{cell_x + cell_size / 2}" y="{cell_y + cell_size / 2 + 9}" class="count-text" text-anchor="middle" fill="{text_fill}">{count}</text>'
            )

    fragments.append(svg_text(440, 2760, "Key reading", "axis-label"))
    fragments.append(svg_text(440, 2792, "Structure <-> Degradation = 5 is the strongest coupling in the landscape.", "legend-text"))
    fragments.append(svg_text(440, 2822, "Location remains isolated: every Location pairing is supported by only one tradition (SD).", "legend-text"))
    return "\n".join(fragments)


def build_svg() -> str:
    level1_fragment, row_centers, badge_centers = draw_level1()
    level2_fragment, property_centers = draw_level2(row_centers, badge_centers)
    level3_fragment = draw_level3(property_centers)
    return f'''<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-head" viewBox="0 0 10 10" refX="8.3" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1 1 L 9 5 L 1 9" fill="none" stroke="#334155" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <style>
      .title {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 34px; font-weight: 700; fill: #18212A; }}
      .subtitle {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 17px; fill: #4E5D6C; }}
      .section-title {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 26px; font-weight: 700; fill: #1E2935; }}
      .section-note {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 16px; fill: #607181; }}
      .axis-label {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 700; fill: #334155; }}
      .row-label {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 17px; fill: #253242; }}
      .column-label {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 13px; font-weight: 700; fill: #253242; }}
      .legend-text {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 15px; fill: #4B5A69; }}
      .chip-label {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 12px; font-weight: 700; }}
      .chip-label-muted {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 12px; font-weight: 700; }}
      .mini-chip-label {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 11px; font-weight: 700; }}
      .count-text {{ font-family: 'Aptos', 'Segoe UI', sans-serif; font-size: 28px; font-weight: 700; }}
    </style>
  </defs>
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#FFFFFF"/>
  {level1_fragment}
  {level2_fragment}
  {level3_fragment}
</svg>
'''


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    SVG_PATH.write_text(build_svg(), encoding="utf-8")
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()