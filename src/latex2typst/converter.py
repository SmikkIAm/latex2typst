import re


def convert(latex: str) -> str:
    """Convert LaTeX source to Typst markup."""
    return re.sub(r"\\section\{(.*?)\}", r"= \1", latex)
