from typing import Iterable
from alloc_lang_runtime.EventData import EventData
from ast_nodes.alloc_lang_primitives import Node

class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def get_live_nodes(self, found=None):
        if (found is None):
            found = []
        return found + self.expr.get_live_nodes()

    def update(self, name: str, value: float):
        self.expr.update(name, value)

    def evaluate(self, event_data: EventData) -> dict:
        return self.expr.evaluate(event_data)


class Block(Node):
    def __init__(self, statements: Iterable[Statement]):
        self.statements = statements

    def get_live_nodes(self, found=None):
        if (found is None):
            found = []

        for statement in self.statements:
            found += statement.get_live_nodes()
        return found

    def update(self, name: str, value: float):
        for statement in self.statements:
            statement.update(name, value)

    def evaluate(self, event_data: EventData) -> dict:
        for statement in self.statements:
            # print(event_data)
            event_data = statement.evaluate(event_data)
        return event_data