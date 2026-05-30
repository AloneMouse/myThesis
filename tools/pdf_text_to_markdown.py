from __future__ import print_function

import argparse
import os
import re
import sys

from PyPDF2 import PdfReader


SPECIAL_TOKENS = [
    ("/summationtext", "\\sum"),
    ("/summationdisplay", "\\sum"),
    ("/integraldisplay", "\\int"),
    ("/integraltext", "\\int"),
    ("/negationslash", "\\ne "),
    ("/logicaland", "\\wedge "),
    ("/logicalor", "\\vee "),
    ("/lessequal", "\\le "),
    ("/greaterequal", "\\ge "),
    ("/partialdiff", "\\partial "),
    ("/gradient", "\\nabla "),
    ("/infinity", "\\infty "),
    ("/plusminus", "\\pm "),
    ("/minusplus", "\\mp "),
    ("/degree", "^\\circ "),
    ("/alpha", "\\alpha "),
    ("/beta", "\\beta "),
    ("/gamma", "\\gamma "),
    ("/delta", "\\delta "),
    ("/epsilon", "\\epsilon "),
    ("/theta", "\\theta "),
    ("/lambda", "\\lambda "),
    ("/mu", "\\mu "),
    ("/pi", "\\pi "),
    ("/rho", "\\rho "),
    ("/sigma", "\\sigma "),
    ("/tau", "\\tau "),
    ("/phi", "\\phi "),
    ("/omega", "\\omega "),
]


SECTION_RE = re.compile(
    r"^((?:[IVXLCDM]+|[0-9]+)(?:\.[0-9]+)*\.?|[A-Z])\s+([A-Z][A-Za-z0-9,;:()'’\-/ ]{3,})$"
)
NUMBERED_TITLE_RE = re.compile(r"^[0-9]+(?:\.[0-9]+)*\.?\s+\S")
TABLE_MARKER_RE = re.compile(r"^(table|tab\.|TABLE|Tab\.)\s+[IVXLCDM0-9]+", re.I)
FIGURE_MARKER_RE = re.compile(r"^(fig\.|figure)\s+[IVXLCDM0-9]+", re.I)
REFERENCES_RE = re.compile(r"^(references|bibliography)$", re.I)


def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name.rstrip(". ") or "document"


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def iter_pdfs(source_dir):
    for root, _, files in os.walk(source_dir):
        for filename in sorted(files):
            if filename.lower().endswith(".pdf"):
                yield os.path.join(root, filename)


def normalize_math_tokens(text):
    for source, replacement in SPECIAL_TOKENS:
        text = text.replace(source, replacement)
    text = text.replace("≤", "\\le ")
    text = text.replace("≥", "\\ge ")
    text = text.replace("≠", "\\ne ")
    text = text.replace("∑", "\\sum ")
    text = text.replace("∫", "\\int ")
    text = text.replace("∞", "\\infty ")
    text = text.replace("∂", "\\partial ")
    text = text.replace("∇", "\\nabla ")
    return text


def normalize_text(text):
    text = normalize_math_tokens(text)
    text = text.replace("\u00ad\n", "")
    text = text.replace("\u00ad", "")
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("−", "-").replace("·", " * ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def extract_page_lines(page):
    chunks = []

    def visitor_text(text, cm, tm, font_dict, font_size):
        if not text:
            return
        normalized = normalize_text(text)
        for raw in normalized.split("\n"):
            line = raw.strip()
            if line:
                chunks.append(
                    {
                        "x": float(tm[4]),
                        "y": float(tm[5]),
                        "size": float(font_size or 0),
                        "text": line,
                    }
                )

    try:
        page.extract_text(visitor_text=visitor_text)
    except TypeError:
        text = normalize_text(page.extract_text() or "")
        return [
            {"x": 0.0, "y": float(-index), "size": 10.0, "text": line.strip()}
            for index, line in enumerate(text.splitlines())
            if line.strip()
        ]

    if not chunks:
        text = normalize_text(page.extract_text() or "")
        return [
            {"x": 0.0, "y": float(-index), "size": 10.0, "text": line.strip()}
            for index, line in enumerate(text.splitlines())
            if line.strip()
        ]

    chunks.sort(key=lambda item: (-round(item["y"], 1), item["x"]))
    lines = []
    current = None
    tolerance = 2.0
    for item in chunks:
        if current is None or abs(current["y"] - item["y"]) > tolerance:
            if current is not None:
                current["text"] = current["text"].strip()
                lines.append(current)
            current = {
                "x": item["x"],
                "y": item["y"],
                "size": item["size"],
                "text": item["text"],
                "sizes": [item["size"]],
            }
        else:
            gap = item["x"] - (current["x"] + len(current["text"]) * current["size"] * 0.45)
            sep = "    " if gap > 24 else " "
            current["text"] += sep + item["text"]
            current["sizes"].append(item["size"])
            current["size"] = max(current["sizes"])
    if current is not None:
        current["text"] = current["text"].strip()
        lines.append(current)
    return lines


def extract_plain_lines(page):
    text = normalize_text(page.extract_text() or "")
    lines = []
    for raw in text.splitlines():
        line = re.sub(r"[ \t]+", " ", raw).strip()
        if line:
            lines.append({"x": 0.0, "y": 0.0, "size": 10.0, "text": line})
    return lines


def is_noise_line(line):
    text = line["text"].strip()
    if not text:
        return True
    if re.match(r"^\d+$", text):
        return True
    if "Downloaded from" in text or "Authorized licensed use" in text:
        return True
    if re.match(r"^(IEEE|Transportation Research|Expert Systems With Applications).*(VOL\.|Vol\.)", text):
        return True
    return False


def is_probable_title(line, page_index):
    text = line["text"].strip()
    if page_index == 0 and line["size"] >= 12 and len(text) > 12:
        return True
    return False


def heading_level(text, size, page_index):
    clean = text.strip(" .")
    if page_index == 0 and size >= 12 and len(clean) > 12:
        return 1
    if REFERENCES_RE.match(clean):
        return 2
    if SECTION_RE.match(clean) and (clean.upper() == clean or NUMBERED_TITLE_RE.match(clean)):
        if re.match(r"^[IVXLCDM]+\.?\s+", clean) or re.match(r"^[0-9]+\.?\s+", clean):
            return 2
        return 3
    if NUMBERED_TITLE_RE.match(clean) and size >= 10:
        depth = clean.split()[0].strip(".").count(".")
        return min(4, 2 + depth)
    if TABLE_MARKER_RE.match(clean) or FIGURE_MARKER_RE.match(clean):
        return 4
    return 0


def looks_like_math(text):
    stripped = text.strip()
    if len(stripped) < 8:
        return False
    strong_math = [
        "=",
        "\\sum",
        "\\int",
        "\\le",
        "\\ge",
        "\\ne",
        "\\partial",
        "\\nabla",
        "^",
        "_",
    ]
    if not any(token in stripped for token in strong_math):
        return False
    if len(stripped.split()) > 34:
        return False
    if re.search(r"[A-Za-z][0-9]?\s*\([a-zA-Zt]\)", stripped):
        return True
    if re.search(r"[A-Za-z0-9]\s*(=|\\le|\\ge|\\ne)\s*", stripped):
        return True
    if re.search(r"\([0-9]{1,3}\)$", stripped) and any(token in stripped for token in ["=", "\\sum", "\\int", "\\le", "\\ge", "\\ne"]):
        return True
    return any(token in stripped for token in ["\\sum", "\\int", "\\partial", "\\nabla"])


def split_table_row(text):
    compact = re.sub(r"\s+", " ", text).strip()
    match = re.match(r"^(\S.{0,28}?)\s{2,}(.+)$", text)
    if match:
        return [match.group(1).strip(), match.group(2).strip()]
    match = re.match(
        r"^((?:[\ue000-\uf8ff]|[A-Za-z]?[A-Za-z0-9_]*(?:\s*\([^)]*\))?|\S{1,12}))\s+([A-Z][A-Za-z].+)$",
        compact,
    )
    if match and len(compact.split()) >= 4:
        return [match.group(1).strip(), match.group(2).strip()]
    return None


def flush_paragraph(lines, output):
    if not lines:
        return
    paragraph = " ".join(lines)
    paragraph = re.sub(r"-\s+", "", paragraph)
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    if paragraph:
        output.append(paragraph)
        output.append("")
    del lines[:]


def flush_table(rows, output):
    if not rows:
        return
    max_cols = max(len(row) for row in rows)
    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    if max_cols >= 2 and len(normalized) >= 2:
        output.append("| " + " | ".join(normalized[0]) + " |")
        output.append("| " + " | ".join(["---"] * max_cols) + " |")
        for row in normalized[1:]:
            output.append("| " + " | ".join(row) + " |")
        output.append("")
    else:
        output.extend(["    " + "    ".join(row) for row in normalized])
        output.append("")
    del rows[:]


def pdf_to_markdown(pdf_path):
    reader = PdfReader(pdf_path)
    output = []
    paragraph = []
    table_rows = []
    emitted_title = True
    table_mode = False
    table_gap = 0

    output.append("---")
    output.append("source_pdf: {}".format(os.path.basename(pdf_path).replace("\\", "\\\\")))
    output.append("pages: {}".format(len(reader.pages)))
    output.append("---")
    output.append("")
    output.append("# {}".format(os.path.splitext(os.path.basename(pdf_path))[0]))
    output.append("")

    for page_index, page in enumerate(reader.pages):
        lines = extract_plain_lines(page)
        output.append("<!-- page {} -->".format(page_index + 1))
        output.append("")

        for line in lines:
            if is_noise_line(line):
                continue
            text = line["text"].strip()
            if not text:
                continue

            level = heading_level(text, line["size"], page_index)
            if page_index == 0 and level == 1:
                level = 0
            if level:
                flush_paragraph(paragraph, output)
                flush_table(table_rows, output)
                table_mode = TABLE_MARKER_RE.match(text.strip()) is not None
                table_gap = 0
                if level == 1 and emitted_title:
                    level = 2
                emitted_title = emitted_title or level == 1
                output.append("{} {}".format("#" * level, text.strip()))
                output.append("")
                continue

            if is_probable_title(line, page_index) and not emitted_title:
                flush_paragraph(paragraph, output)
                flush_table(table_rows, output)
                emitted_title = True
                table_mode = False
                table_gap = 0
                output.append("# {}".format(text))
                output.append("")
                continue

            row = split_table_row(text) if table_mode else None
            if row and len(row) <= 6:
                flush_paragraph(paragraph, output)
                table_rows.append(row)
                table_gap = 0
                continue
            elif table_rows:
                table_gap += 1
                if table_gap > 2 or level:
                    flush_table(table_rows, output)
                    table_mode = False
                    table_gap = 0

            if looks_like_math(text):
                flush_paragraph(paragraph, output)
                output.append("$$")
                output.append(text)
                output.append("$$")
                output.append("")
                continue

            paragraph.append(text)

        flush_paragraph(paragraph, output)
        flush_table(table_rows, output)

    return "\n".join(output).rstrip() + "\n"


def convert_all(source_dir, output_dir):
    source_dir = os.path.abspath(source_dir)
    output_dir = os.path.abspath(output_dir)
    ensure_dir(output_dir)

    pdfs = list(iter_pdfs(source_dir))
    for index, pdf_path in enumerate(pdfs, 1):
        rel_dir = os.path.relpath(os.path.dirname(pdf_path), source_dir)
        if rel_dir == ".":
            rel_dir = ""
        destination_dir = os.path.join(output_dir, rel_dir)
        ensure_dir(destination_dir)
        base = sanitize_filename(os.path.splitext(os.path.basename(pdf_path))[0])
        markdown_path = os.path.join(destination_dir, base + ".md")
        print("[{}/{}] {}".format(index, len(pdfs), markdown_path))
        markdown = pdf_to_markdown(pdf_path)
        with open(markdown_path, "wb") as handle:
            handle.write(markdown.encode("utf-8"))
    return len(pdfs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="papers")
    parser.add_argument("--output", default="markdown_docs")
    args = parser.parse_args()
    count = convert_all(args.source, args.output)
    print("Converted {} PDF file(s).".format(count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
