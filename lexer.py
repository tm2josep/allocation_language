import re
from rply import LexerGenerator

lexer_rules = [
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("ALLOC", r"alloc"),
    ("NEWLINE", r"\n"),
    ("PERCENT", r"\%((\d+\.\d+)|(\d+)|(\.\d+))"),
    ("INT", r"\d+"),
    ("FLOAT", r"[+-]?([0-9]*[.])?[0-9]+"),
    ("FIELD_NAME", r"@\'.+?'"),
    ("VAR_NAME", r"\$[A-Za-z]+[0-9]+")
]

def get_lexer_tokens():
    return [name for name, _ in lexer_rules]

def make_new_lexer():
    lg = LexerGenerator()

    lg.ignore(r"[^\S\r\n]")
    for name, regex in lexer_rules:
        lg.add(name, regex)

    lexer = lg.build()
    return lexer
