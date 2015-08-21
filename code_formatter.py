# -*- coding: utf-8 -*-

import codecs

from pygments import highlight
from pygments.lexers import (
    PythonLexer,
    PythonConsoleLexer,
    PythonTracebackLexer
)
from pygments.formatters import HtmlFormatter


encoding = 'utf-8'
input_filename = 'code1.py'
output_filename = 'snippet.html'

with codecs.open(input_filename, 'r', encoding=encoding) as input_file:
    code = input_file.read()

lexer = PythonConsoleLexer(encoding=encoding, stripall=True)

formatter = HtmlFormatter(
    # linenos=True,
    noclasses=True,
    prestyles="padding: 20px 20px 20px 20px",
    # cssstyles="padding: 20px 20px 20px 20px",
    # hl_lines=[1, 7],
    # cssclass="source",
    style='monokai'
)

with codecs.open(output_filename, 'w', encoding=encoding) as output_file:
    highlight(code, lexer, formatter, outfile=output_file)
