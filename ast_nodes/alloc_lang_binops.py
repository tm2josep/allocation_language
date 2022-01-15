from .alloc_lang_nodes import Node
from .alloc_lang_primitives import Field, LiveVar, Number


class BinOp(Node):
    def __init__(self, node_a: Node, node_b: Node):
        self.rhs: Field | LiveVar | Number = node_a
        self.lhs: Field | LiveVar | Number = node_b
    
    def update(self, name: str, value: float):
        self.rhs.update(name, value)
        self.lhs.update(name, value)

    def evaluate(self, event_data: dict) -> float:
        a = self.rhs.evaluate(event_data)
        b = self.lhs.evaluate(event_data)
        return self.compute(a, b)


class Exponentiate(BinOp):
    def compute(self, a: float, b: float) -> float:
        return a ** b


class Multiply(BinOp):
    def compute(self, a: float, b: float) -> float:
        return a * b


class Divide(BinOp):
    def compute(self, a: float, b: float) -> float:
        return a / b


class Add(BinOp):
    def compute(self, a: float, b: float) -> float:
        return a + b


class Subtract(BinOp):
    def compute(self, a: float, b: float) -> float:
        return a - b
