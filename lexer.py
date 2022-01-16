from rply import LexerGenerator

lexer_rules = [
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("ALLOC", r"alloc"),
    ("SCOPE", r"scope"),
    ("ASSESS", r"assess"),
    ("NEWLINE", r"\n"),
    ("PERCENT", r"\%"),
    ("NUMBER", r"(\-)?((\d+\.\d+)|(\.\d+)|(\d+))"),
    ("FIELD_START", r"@'"),
    ("FIELD_END", r"(?<!\\)(?:(\\\\)*)[']"), # Lookbehind makes sure we don't match an escaped '
    ("AGG_MODE", r"\:((sum)|(mean)|(median)|(mode)|(max)|(min)|(count))"),
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
