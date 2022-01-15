import custom_exceptions


class Node(object):
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

    def update(self, name: str, value: float):
        pass

    def evaluate(self, event_data: dict) -> dict | float:
        return event_data


class Percent(Node):
    def __init__(self, string_value: str):
        self.num_value = float(string_value) / 100

    def evaluate(self, _: dict) -> float:
        return self.num_value


class Number(Node):
    def __init__(self, string_value: str):
        self.num_value = float(string_value)

    def evaluate(self, _: dict) -> float:
        return self.num_value


class Field(Node):
    def __init__(self, string_name: str):
        self.name = string_name

    def evaluate(self, event_data: dict) -> float:
        if self.name not in event_data:
            raise custom_exceptions.FieldNotInDataError(event_data, self.name)
        return event_data[self.name]


class LiveVar(Node):
    def __init__(self, string_name: str):
        self.name = string_name
        self.num_value: float = 0.0

    # Catch any valid updates that are sent down the tree
    def update(self, name: str, value: float):
        if self.name == name:
            self.num_value = value

    def evaluate(self, _: dict) -> float:
        return self.num_value
