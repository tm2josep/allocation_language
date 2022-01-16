from alloc_lang_runtime.event_dataclasses import EventData
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
    contract = make_contract("./test_files/test1.alg")

    contract.update("test", 1e5)

    events = contract.evaluate_stream(event_stream())
    for event in events:
        print(event)
        pass
        # print(event)
    print(contract.get_live_nodes())


if __name__ == "__main__":
    main()
