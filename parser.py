from rply import ParserGenerator
import lexer
import ast_nodes.all_nodes as ast

pg = ParserGenerator(lexer.get_lexer_tokens(), cache_id="alloc_lang")

# MAIN STATEMENTS
@pg.production("main : statements")
def main(s):
    return s[0]

@pg.production("statements : statement EOL statements")
def statments(s):
    return ast.Block([s[0]] + [s[2]])

@pg.production("statements : statement EOL")
def statements_statement_eol(s):
    return ast.Statement(s[0])

# COMMAND: "assess"
@pg.production("statement : ASSESS agg_field")
def assess_start(s):
    return ast.AssessNode(s[1])

# COMMAND: "alloc"
@pg.production("statement : ALLOC field expr field")
def alloc_fields_int(s):
    return ast.Alloc(s[1], s[2], s[3])

# COMMAND: "aggregate"
@pg.production("statement : AGGREGATE agg_fields")
def aggregation_keyless(s):
    return ast.KeylessAggregateNode(s[1])

@pg.production("statement : AGGREGATE KEY field agg_fields")
def aggregation_keyed(s):
    return ast.KeyedAggregateNode(s[2], s[3])

@pg.production("agg_fields : agg_field agg_fields")
def aggregation_fields(s):
    return [s[0]] + s[1]

@pg.production("agg_fields : agg_field")
def aggregation_fields_end(s):
    return [s[0]]

# COMMAND: "scope"
@pg.production("statement : SCOPE condition")
def scope_command(s):
    return ast.Scope(s[1])

@pg.production("condition : condition AND condition")
def conditional_and(s):
    return ast.AndNode(s[0], s[2])

@pg.production("condition : condition OR condition")
def conditional_or(s):
    return ast.OrNode(s[0], s[2])

@pg.production("condition : LPAREN condition RPAREN")
def conditional_wrapped(s):
    return s[1]

@pg.production("condition : expr COMPARATOR expr")
def condition_compare(s):
    return ast.Condition(s[0], s[1].getstr(), s[2])

# COMMAND: "discard"
@pg.production("statement : DISCARD condition")
def discard_command(s):
    return ast.DiscardNode(s[1])

# EXPRESSION MANAGEMENT
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

# NAME MANAGMENT
@pg.production("field : FIELD_START NAME FIELD_END")
def field_name(s):
    return ast.Field(s[1].getstr())

@pg.production("agg_field : FIELD_START NAME FIELD_END AGG_MODE")
def aggregate_field(s):
    return ast.AggField(s[1].getstr(), s[3].getstr()[1:])

@pg.production("value : VAR_START NAME")
def live_var_name(s):
    return ast.LiveVar(s[1].getstr())


# CONSTANTS AND VALUES
@pg.production("value : NUMBER")
def num_value(s):
    return ast.Number(s[0].getstr())

@pg.production("value : NUMBER PERCENT")
def percent_value(s):
    return ast.Percent(s[0].getstr())

@pg.production("value : STRING")
def string_value(s):
    return ast.String(s[0].getstr()[1:-1])

parser = pg.build()