from rply import ParserGenerator
import lexer
import ast_nodes.all_nodes as ast

pg = ParserGenerator(lexer.get_lexer_tokens(), cache_id="alloc_lang")

@pg.production("main : statements")
def main(s):
    return s[0]

@pg.production("statements : statement NEWLINE statements")
def statments(s):
    return ast.Block([s[0]] + [s[2]])

@pg.production("statements : statement NEWLINE")
def statements_statement_eol(s):
    return ast.Statement(s[0])

@pg.production("statements : statement")
def statements_statement(s):
    return ast.Statement(s[0])

@pg.production("statement : ALLOC field expr field")
def alloc_fields_int(s):
    return ast.Alloc(s[1], s[2], s[3])

@pg.production("expr : LPAREN expr RPAREN")
def parenthesized_expression(s):
    return s[1]

@pg.production("expr : expr EXP expr")
def expression_product(s):
    return ast.Exponentiate(s[0], s[2])

@pg.production("expr : expr MULT expr")
def expression_product(s):
    return ast.Multiply(s[0], s[2])

@pg.production("expr : expr DIV expr")
def expression_product(s):
    return ast.Divide(s[0], s[2])

@pg.production("expr : expr ADD expr")
def expression_product(s):
    return ast.Add(s[0], s[2])

@pg.production("expr : expr SUB expr")
def expression_product(s):
    return ast.Subtract(s[0], s[2])

@pg.production("expr : value")
def expression_value(s):
    return s[0]

@pg.production("value : field")
def field_as_value(s):
    return s[0]

@pg.production("field : FIELD_START NAME FIELD_END")
def field_name(s):
    return ast.Field(s[1].getstr())

@pg.production("value : VAR_START NAME")
def live_var_name(s):
    return ast.LiveVar(s[1].getstr())

@pg.production("value : NUMBER")
def int_value(s):
    return ast.Number(s[0].getstr())

@pg.production("value : NUMBER PERCENT")
def percent_value(s):
    return ast.Percent(s[0].getstr())


parser = pg.build()
