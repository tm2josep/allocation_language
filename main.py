import lexer as lexer_module
from parser import parser

def make_contract(file_src):
    with open('./test_files/test1.alg', 'r') as src_file:
        lexer = lexer_module.make_new_lexer()
        token_stream = lexer.lex(src_file.read())

        syntax_tree = parser.parse(token_stream)
        return syntax_tree

def main():
    syntax_tree = make_contract('./test_files/test1.alg')

    syntax_tree.update('test', 0.5)
    print(syntax_tree.evaluate({"claim": 100, "liable": 0}))
    
    syntax_tree.update('test', 10)
    print(syntax_tree.evaluate({"claim": 100, "liable": 0}))

if (__name__ == '__main__'):
    main()