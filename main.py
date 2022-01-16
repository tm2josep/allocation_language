from alloc_lang_runtime.EventData import EventData
import lexer as lexer_module
from parser import parser
import random

def make_contract(file_src):
    with open("./test_files/test1.alg", "r") as src_file:
        lexer = lexer_module.make_new_lexer()
        token_stream = lexer.lex(src_file.read())

        syntax_tree = parser.parse(token_stream)
        return syntax_tree


def event_stream():
    for n in range(5000):
        yield EventData(
            data = {
                "claim": random.randint(1, 5e5),
                "liable": 0
            }
        )

def main():
    syntax_tree = make_contract("./test_files/test1.alg")

    syntax_tree.update("test", 1e5)

    for loss in syntax_tree.evaluate_stream(event_stream()):
        print(loss)
    print(syntax_tree.get_live_nodes())


if __name__ == "__main__":
    main()
