from rply import ParserGenerator
import lexer
import alloc_lang_nodes as ast

pg = ParserGenerator(lexer.get_lexer_tokens(), cache_id="alloc_lang")

@pg.production("main : statements")
def main(s):
    return s[0]

@pg.production("statements : statement NEWLINE statements")
def statments(s):
    return ast.Block([s[0]] + [s[2]])

@pg.production("statements : statement NEWLINE")
def statements_statement(s):
    return ast.Statement(s[0])

@pg.production("statements : statement")
def statements_statement(s):
    return ast.Statement(s[0])
    
@pg.production("statement : ALLOC FIELD_NAME value FIELD_NAME")
def alloc_fields_int(s):
    return ast.Alloc(
        ast.Field(s[1].getstr()), 
        s[2], 
        ast.Field(s[3].getstr())
    )

@pg.production("value : VAR_NAME")
def live_var_name(s):
    return ast.LiveVar(s[0].getstr())

@pg.production("value : INT")
def int_value(s):
    return ast.Number(s[0].getstr())

@pg.production("value : FLOAT")
def int_value(s):
    return ast.Number(s[0].getstr())

@pg.production("value : PERCENT")
def percent_value(s):
    return ast.Percent(s[0].getstr())

@pg.production("value : FIELD_NAME")
def live_var_name(s):
    return ast.Field(s[0].getstr())

parser = pg.build()