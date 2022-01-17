from alloc_lang_runtime.event_dataclasses import AssessmentEvent, EventData
import lexer as lexer_module
from parser import parser
import random

def make_contract(file_src):
    with open("./test_files/test1.txt", "r") as src_file:
        lexer = lexer_module.make_new_lexer()
        token_stream = lexer.lex(src_file.read())

        syntax_tree = parser.parse(token_stream)
        return syntax_tree

def event_stream():
    for _ in range(5000):
        yield EventData(
            data = {
                "type": random.choice(['A', 'B', 'C']),
                "claim": random.randint(1, 5e5),
                "liable": 0
            }
        )

def main():
    contract = make_contract("./test_files/test1.alg")
    contract.update("test", 1e5)
    events = contract.evaluate_stream(event_stream())

    total = 0
    for event in events:
        if (isinstance(event, AssessmentEvent)):
            print(event)
            total += event.final_value

    print(f"{total:,.2f}")


if __name__ == "__main__":
    main()
