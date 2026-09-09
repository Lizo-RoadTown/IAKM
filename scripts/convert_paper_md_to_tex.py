from __future__ import annotations

import re
import sys
from pathlib import Path


PAPER_CONFIG = {
    "paper1": {
        "documentclass": "\\documentclass[journal]{IEEEtran}",
        "packages": [
            "\\usepackage{amsmath}",
            "\\usepackage{amssymb}",
            "\\usepackage{graphicx}",
            "\\usepackage{booktabs}",
            "\\usepackage{tabularx}",
            "\\usepackage{array}",
            "\\usepackage{hyperref}",
            "\\usepackage{url}",
            "\\usepackage{cite}",
        ],
        "table_env": "table*",
        "table_width": "\\textwidth",
        "table_position": "!t",
        "figure_width": "\\columnwidth",
        "figure_position": "!t",
        "title": "Locating Knowledge at Structural Interfaces: Knowledge Type, Interface Properties, and Structural Distance in a Modular Aerospace System",
        "author": """\\author{
\\IEEEauthorblockN{E.~Osborn}
\\IEEEauthorblockA{California State Polytechnic University, Pomona}
\\and
\\IEEEauthorblockN{M.~Pham}
\\IEEEauthorblockA{Open Source Space Foundation; currently at Vast Space}
\\and
\\IEEEauthorblockN{G.~Placencia}
\\IEEEauthorblockA{California State Polytechnic University, Pomona}
}""",
        "front_matter": [],
        "figure_map": {
            "1": "figures/paper1_figure_instrument_view.pdf",
        },
    },
    "paper3": {
        "documentclass": "\\documentclass[12pt]{article}",
        "packages": [
            "\\usepackage[letterpaper, margin=1in]{geometry}",
            "\\usepackage{amsmath}",
            "\\usepackage{amssymb}",
            "\\usepackage{graphicx}",
            "\\usepackage{booktabs}",
            "\\usepackage{tabularx}",
            "\\usepackage{array}",
            "\\usepackage{float}",
            "\\usepackage[section]{placeins}",
            "\\usepackage{hyperref}",
            "\\usepackage{url}",
            "\\usepackage[authoryear,round]{natbib}",
            "\\usepackage{wasysym}",
        ],
        "table_env": "table",
        "table_width": "\\textwidth",
        "table_position": "H",
        "figure_width": "\\textwidth",
        "figure_position": "H",
        "title": "The Structural Properties of Knowledge: Tracing Convergence Across Disciplinary Boundaries",
        "author": """\\author{
  Osborn, E.\\textsuperscript{1} \\and Placencia, G.\\textsuperscript{1} \\and Pham, M.\\textsuperscript{2,3}
}""",
        "front_matter": [
            "\\noindent\\textsuperscript{1}California State Polytechnic University, Pomona.\\\\",
            "\\noindent\\textsuperscript{2}Open Source Space Foundation.\\\\",
            "\\noindent\\textsuperscript{3}Currently at Vast Space.",
            "",
            "\\vspace{1em}",
        ],
        "figure_map": {},
    },
}


SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def escape_latex(text: str) -> str:
    return "".join(SPECIALS.get(char, char) for char in text)


def sanitize_label(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "item"


def strip_formatting(text: str) -> str:
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text.strip()


def convert_inline(text: str) -> str:
    placeholders: list[str] = []

    def stash(pattern: str, template: str, source: str) -> str:
        def repl(match: re.Match[str]) -> str:
            placeholders.append(template.format(convert_inline(match.group(1))))
            return f"@@PLACEHOLDER{len(placeholders) - 1}@@"

        return re.sub(pattern, repl, source)

    text = stash(r"`([^`]+)`", r"\texttt{{{}}}", text)
    text = stash(r"\*\*\*(.+?)\*\*\*", r"\textbf{{\textit{{{}}}}}", text)
    text = stash(r"\*\*(.+?)\*\*", r"\textbf{{{}}}", text)
    text = stash(r"\*(.+?)\*", r"\textit{{{}}}", text)
    text = escape_latex(text)
    text = re.sub(r"\^([A-Za-z0-9]+)", r"\textsuperscript{\1}", text)
    text = text.replace("--", "---")
    for index, replacement in enumerate(placeholders):
        text = text.replace(f"@@PLACEHOLDER{index}@@", replacement)
    return text


def strip_heading_number(text: str) -> str:
    return re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", text).strip()


def split_metadata(lines: list[str]) -> tuple[list[str], list[str]]:
    body_start = 0
    for index, line in enumerate(lines):
        if line.startswith("# Abstract"):
            body_start = index
            break
    return lines[:body_start], lines[body_start:]


def build_table_alignment(header: list[str], data_rows: list[list[str]]) -> str:
    compact_headers = {"rank", "year", "status", "results", "section", "sections"}
    compact_column = "@{}>{\\raggedright\\arraybackslash}p{0.12\\textwidth}@{}"
    flexible_column = ">{\\raggedright\\arraybackslash}X"
    column_specs: list[str] = []

    for index, title in enumerate(header):
        values = [strip_formatting(row[index]) for row in data_rows if index < len(row)]
        longest_value = max((len(value) for value in values), default=0)
        header_name = strip_formatting(title).lower()
        if header_name in compact_headers or longest_value <= 12:
            column_specs.append(compact_column)
        else:
            column_specs.append(flexible_column)

    return "".join(column_specs)


def append_block(out: list[str], block: list[str]) -> None:
    out.extend(block)
    if out and out[-1] != "":
        out.append("")


def parse_table(lines: list[str], start: int, config: dict[str, object]) -> tuple[list[str], int]:
    caption = strip_formatting(lines[start])
    index = start + 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    table_lines = []
    while index < len(lines) and lines[index].startswith("|"):
        table_lines.append(lines[index])
        index += 1
    notes = []
    while index < len(lines) and lines[index].startswith("^"):
        notes.append(lines[index])
        index += 1
    if len(table_lines) < 2:
        return [convert_inline(caption)], index

    rows = []
    for row in table_lines:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        rows.append(cells)

    header = rows[0]
    data_rows = [row for row in rows[2:]]
    col_count = len(header)
    alignment = build_table_alignment(header, data_rows)
    env = str(config.get("table_env") or ("table*" if col_count > 4 else "table"))
    width = str(config.get("table_width") or ("\\textwidth" if env == "table*" else "\\columnwidth"))
    position = str(config.get("table_position", "!t"))
    label = sanitize_label(caption)

    out = [
        rf"\begin{{{env}}}[{position}]",
        rf"\caption{{{convert_inline(caption)}}}",
        rf"\label{{tab:{label}}}",
        "\\centering",
        "{\\small",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\renewcommand{\\arraystretch}{1.1}",
        rf"\begin{{tabularx}}{{{width}}}{{{alignment}}}",
        "\\toprule",
        " " + " & ".join(convert_inline(cell) for cell in header) + r" \\",
        "\\midrule",
    ]
    for row in data_rows:
        padded = row + [""] * (col_count - len(row))
        out.append(" " + " & ".join(convert_inline(cell) for cell in padded[:col_count]) + r" \\")
    out.extend([
        "\\bottomrule",
        "\\end{tabularx}",
        "}",
    ])
    if notes:
        out.append("\\vspace{0.5em}")
        out.append("{\\footnotesize")
        for note in notes:
            marker, _, note_text = note.partition(" ")
            out.append(rf"\noindent\textsuperscript{{{marker[1:]}}} {convert_inline(note_text)}\\")
        out.append("}")
    out.append(rf"\end{{{env}}}")
    return out, index


def resolve_figure_path(image_path: str) -> str:
    candidate = Path(image_path)
    if candidate.exists():
        return candidate.as_posix()

    figures_candidate = Path("figures") / image_path
    if figures_candidate.exists():
        return figures_candidate.as_posix()

    if candidate.suffix.lower() == ".svg":
        for extension in (".pdf", ".png", ".jpg", ".jpeg"):
            alt = candidate.with_suffix(extension)
            if alt.exists():
                return alt.as_posix()
            figures_alt = (Path("figures") / candidate.name).with_suffix(extension)
            if figures_alt.exists():
                return figures_alt.as_posix()

    return image_path


def parse_figure(lines: list[str], start: int, config: dict[str, object]) -> tuple[list[str], int]:
    line = lines[start]
    index = start
    image_match = re.match(r"!\[(.*?)\]\((.*?)\)", line)
    figure_number = None
    image_path = None
    caption = None
    if image_match:
        image_path = resolve_figure_path(image_match.group(2).strip())
        index += 1
    else:
        placeholder_match = re.match(r"\*\*\[Fig\.\s*(\d+):\s*(.+?)\]\*\*", line)
        if placeholder_match:
            figure_number = placeholder_match.group(1)
            image_path = config["figure_map"].get(figure_number)
            index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines):
        caption_match = re.match(r"\*\*Fig\.\s*(\d+)\.\*\*\s*(.+)", lines[index])
        if caption_match:
            figure_number = figure_number or caption_match.group(1)
            caption = caption_match.group(2).strip()
            index += 1

    if not image_path and not caption:
        return [convert_inline(line)], start + 1

    caption = caption or image_match.group(1) if image_match else caption
    label = sanitize_label(f"fig-{figure_number or 'item'}")
    figure_position = str(config.get("figure_position", "!t"))
    figure_width = str(config.get("figure_width", "\\columnwidth"))
    out = [rf"\begin{{figure}}[{figure_position}]", "\\centering"]
    if image_path:
        ext = Path(image_path).suffix.lower()
        if ext in {".pdf", ".png", ".jpg", ".jpeg"}:
            out.append(rf"\includegraphics[width={figure_width}]{{{image_path}}}")
        else:
            out.append(rf"\fbox{{\parbox{{0.9{figure_width}}}{{Figure source requires external conversion: {convert_inline(image_path)}}}}}")
    if caption:
        out.append(rf"\caption{{{convert_inline(caption)}}}")
    out.append(rf"\label{{fig:{label}}}")
    out.append("\\end{figure}")
    return out, index


def parse_list(lines: list[str], start: int, ordered: bool) -> tuple[list[str], int]:
    index = start
    env = "enumerate" if ordered else "itemize"
    pattern = r"^\d+\.\s+" if ordered else r"^[-*]\s+"
    out = [rf"\begin{{{env}}}"]
    while index < len(lines):
        line = lines[index]
        if not re.match(pattern, line):
            break
        item = re.sub(pattern, "", line)
        out.append(rf"\item {convert_inline(item)}")
        index += 1
    out.append(rf"\end{{{env}}}")
    return out, index


def parse_paragraph(lines: list[str], start: int) -> tuple[list[str], int]:
    index = start
    parts = []
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            break
        if line.startswith(("#", "***Table", "***TABLE", "![")):
            break
        if re.match(r"\*\*\[Fig\.", line) or re.match(r"\*\*Fig\.", line):
            break
        if re.match(r"^\d+\.\s+", line) or re.match(r"^[-*]\s+", line):
            break
        parts.append(line.strip())
        index += 1
    paragraph = " ".join(parts)
    return [convert_inline(paragraph)], index


def convert_body(lines: list[str], config: dict[str, object]) -> list[str]:
    out: list[str] = []
    index = 0
    in_abstract = False
    while index < len(lines):
        line = lines[index].rstrip()
        if not line.strip() or line.strip() == "---":
            index += 1
            continue

        heading_match = re.match(r"^(#{1,3})\s+(.*)", line)
        if heading_match:
            level = len(heading_match.group(1))
            title = strip_heading_number(heading_match.group(2).strip())
            if title == "Abstract":
                out.append("\\begin{abstract}")
                in_abstract = True
                index += 1
                continue
            if in_abstract:
                out.append("\\end{abstract}")
                in_abstract = False
            command = {1: "section", 2: "subsection", 3: "subsubsection"}[level]
            if title == "References":
                break
            out.append(rf"\{command}{{{convert_inline(title)}}}")
            out.append("")
            index += 1
            continue

        if line.startswith(("***Table", "***TABLE")):
            block, index = parse_table(lines, index, config)
            append_block(out, block)
            continue

        if line.startswith("![") or re.match(r"\*\*\[Fig\.", line):
            block, index = parse_figure(lines, index, config)
            append_block(out, block)
            continue

        if re.match(r"\*\*Fig\.\s*\d+\.\*\*", line):
            index += 1
            continue

        if re.match(r"^\d+\.\s+", line):
            block, index = parse_list(lines, index, ordered=True)
            append_block(out, block)
            continue

        if re.match(r"^[-*]\s+", line):
            block, index = parse_list(lines, index, ordered=False)
            append_block(out, block)
            continue

        block, next_index = parse_paragraph(lines, index)
        if next_index == index:
            out.append(convert_inline(line))
            out.append("")
            index += 1
            continue
        append_block(out, block)
        index = next_index

    if in_abstract:
        out.append("\\end{abstract}")
    return out


def convert_references(lines: list[str]) -> list[str]:
    ref_start = None
    for index, line in enumerate(lines):
        if re.match(r"^#\s+References", line):
            ref_start = index + 1
            break
    if ref_start is None:
        return []

    ref_lines = [line.strip() for line in lines[ref_start:] if line.strip() and line.strip() != "---"]
    if not ref_lines:
        return []

    numbered = all(re.match(r"^\[\d+\]", line) or line.startswith("*[") for line in ref_lines)
    out = ["\\section*{References}"]
    if numbered:
        out.append("\\begin{thebibliography}{99}")
        for line in ref_lines:
            if line.startswith("*["):
                out.append(convert_inline(strip_formatting(line)))
                continue
            match = re.match(r"^\[(\d+)\]\s*(.*)", line)
            if not match:
                out.append(convert_inline(line))
                continue
            number, entry = match.groups()
            out.append(rf"\bibitem{{ref{number}}} {convert_inline(entry)}")
        out.append("\\end{thebibliography}")
        return out

    out.append("\\begin{itemize}")
    for line in ref_lines:
        if line.startswith("-"):
            out.append(rf"\item {convert_inline(line[1:].strip())}")
        else:
            out.append(convert_inline(strip_formatting(line)))
    out.append("\\end{itemize}")
    return out


def build_document(style: str, body_lines: list[str]) -> str:
    config = PAPER_CONFIG[style]
    content = [config["documentclass"], *config["packages"], "", "\\begin{document}", ""]
    content.append(f"\\title{{{convert_inline(config['title'])}}}")
    content.append(config["author"])
    content.append("\\date{}")
    content.append("")
    content.append("\\maketitle")
    if config["front_matter"]:
        content.extend(config["front_matter"])
    content.append("")
    content.extend(convert_body(body_lines, config))
    content.append("")
    content.extend(convert_references(body_lines))
    content.append("")
    content.append("\\end{document}")
    return "\n".join(content) + "\n"


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: python scripts/convert_paper_md_to_tex.py <paper1|paper3> <input.md> <output.tex>")
        return 1

    style, input_path, output_path = sys.argv[1:]
    if style not in PAPER_CONFIG:
        print(f"Unsupported style: {style}")
        return 1

    source = Path(input_path)
    if not source.exists():
        print(f"Input file not found: {source}")
        return 1

    lines = source.read_text(encoding="utf-8").splitlines()
    _, body_lines = split_metadata(lines)
    tex = build_document(style, body_lines)
    Path(output_path).write_text(tex, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())