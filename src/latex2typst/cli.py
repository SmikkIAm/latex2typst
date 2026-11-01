import argparse
from pathlib import Path

from latex2typst.converter import convert


def main():
    p = argparse.ArgumentParser(description="Convert LaTeX to Typst")
    p.add_argument("input", help="input .tex file")
    p.add_argument("-o", "--output", help="output .typ file")
    args = p.parse_args()

    result = convert(Path(args.input).read_text(encoding="utf-8"))
    out = Path(args.output) if args.output else Path(args.input).with_suffix(".typ")
    out.write_text(result, encoding="utf-8")
    print(f"Written {out}")
