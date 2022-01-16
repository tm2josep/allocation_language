from rply import LexerGenerator

lexer_rules = [
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("ALLOC", r"alloc"),
    ("SCOPE", r"scope"),
    ("NEWLINE", r"\n"),
    ("PERCENT", r"\%"),
    ("NUMBER", r"(\-)?((\d+\.\d+)|(\.\d+)|(\d+))"),
    ("FIELD_START", r"@'"),
    # Lookbehind makes sure we don't match an escaped '
    ("FIELD_END", r"(?<!\\)(?:(\\\\)*)[']"),
    ("VAR_START", r"\$"),
    ("NAME", r"[A-Za-z]+[0-9A-Za-z]+"),
    ("EXP", r"\^"),
    ("MULT", r"\*"),
    ("DIV", r"\/"),
    ("ADD", r"\+"),
    ("SUB", r"\-"),
    ("AND", r"\&"),
    ("OR", r"\|"),
    ("COMPARATOR", r"(==)|(>=)|(<=)|(>)|(<)")
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
