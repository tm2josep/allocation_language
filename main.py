import lexer
from parser import parser

with open('./test_files/test1.alg', 'r') as src_file:
    lexer = lexer.make_new_lexer()
    token_stream = lexer.lex(src_file.read())

    syntax_tree = parser.parse(token_stream)
    syntax_tree.update('name1', 10)
    
    print(syntax_tree.evaluate({"claim": 100, "liable": 0}))