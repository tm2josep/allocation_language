from typing import Iterable
from .alloc_lang_primitives import Node
class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def update(self, name: str, value: float):
        self.expr.update(name, value)

    def evaluate(self, event_data: dict) -> dict:
        return self.expr.evaluate(event_data)


class Block(Node):
    def __init__(self, statements: Iterable[Statement]):
        self.statements = statements

    def update(self, name: str, value: float):
        for statement in self.statements:
            statement.update(name, value)

    def evaluate(self, event_data: dict) -> dict:
        for statement in self.statements:
            # print(event_data)
            event_data = statement.evaluate(event_data)
        return event_data