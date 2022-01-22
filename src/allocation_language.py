from os import PathLike
from alloc_lang_data_containers.event_dataclasses import AssessmentEvent, EventData
from typing import Iterable
import lexer as lexer_module
from parser import parser
import random


def _make_contract(text_content: str):
    lexer = lexer_module.make_new_lexer()
    token_stream = lexer.lex(text_content)
    
    contract = parser.parse(token_stream)
    return contract
    
def make_contract_from_file(file_src: PathLike):
    with open("./src/test_files/test1.txt", "r") as src_file:
        return _make_contract(src_file.read())

def make_contract_from_text(text_content: str):
    return _make_contract(text_content)

def __event_stream():
    for _ in range(5000):
        yield EventData(
            data = {
                "type": random.choice(['A', 'B', 'C']),
                "claim": random.randint(1, 5e5),
                "liable": 0,
                "revenue": random.randint(1, 5e5)
            }
        )

def main():
    contract = make_contract_from_file("./test_files/test1.alg")
    contract.update("test", 1e5)
    events: Iterable[EventData | AssessmentEvent] = contract.evaluate_stream(__event_stream())

    for event in events:
        print(event)

if __name__ == "__main__":
    main()