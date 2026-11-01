from latex2typst.converter import convert


def test_section():
    assert convert(r"\section{Intro}") == "= Intro"
