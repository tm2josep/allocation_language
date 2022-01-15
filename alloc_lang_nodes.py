from typing import Iterable
import custom_exceptions

class Node(object):
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

    def update(self, name: str, value: float):
        return


class Percent(Node):
    def __init__(self, string_value: str):
        self.num_value = float(string_value[1:]) / 100

class Number(Node):
    def __init__(self, string_value: str):
        self.num_value = float(string_value)

class Field(Node):
    def __init__(self, string_name: str):
        self.name = string_name[2:-1]

    def evaluate(self, event_data: dict):
        if self.name not in event_data:
            raise custom_exceptions.FieldNotInDataError(event_data, self.name)
        return event_data[self.name]


class LiveVar(Node):
    def __init__(self, string_name: str):
        self.name: str = string_name[1:]
        self.num_value: float = 0.0

    # Catch any valid updates that are sent down the tree
    def update(self, name: str, value: float):
        if (self.name == name):
            self.num_value = value

class Alloc(Node):
    def __init__(
        self, source: Field, value_node: Number | Percent | LiveVar, target: Field
    ):
        self.source = source
        self.value_node = value_node
        self.target = target

    def update(self, name: str, value: float):
        self.value_node.update(name, value)

    def modify_data(self, event_data: dict, quantity: float):
        source_val = float(self.source.evaluate(event_data))
        target_val = float(self.target.evaluate(event_data))

        source_val -= quantity
        target_val += quantity

        event_data[self.source.name] = source_val
        event_data[self.target.name] = target_val

        return event_data

    def evaluate_const(self, event_data: dict):
        source_val = float(self.source.evaluate(event_data))
        quantity = min(source_val, self.value_node.num_value)
        return self.modify_data(event_data, quantity)

    def evaluate_share(self, event_data: dict):
        source_val = float(self.source.evaluate(event_data))
        quantity = self.value_node.num_value * source_val
        return self.modify_data(event_data, quantity)

    def evaluate(self, event_data: dict):
        if isinstance(self.value_node, Number):
            return self.evaluate_const(event_data)

        if isinstance(self.value_node, LiveVar):
            return self.evaluate_const(event_data)

        if isinstance(self.value_node, Percent):
            return self.evaluate_share(event_data)


class Statement(Node):
    def __init__(self, expr: Alloc):
        self.expr = expr

    def evaluate(self, event_data: dict):
        return self.expr.evaluate(event_data)

    def update(self, name: str, value: float):
        self.expr.update(name, value)


class Block(Node):
    def __init__(self, statements: Iterable[Statement]):
        self.statements = statements

    def update(self, name: str, value: float):
        for statement in self.statements:
            statement.update(name, value)

    def evaluate(self, event_data: dict):
        for statement in self.statements:
            # print(event_data)
            event_data = statement.evaluate(event_data)
        return event_data
