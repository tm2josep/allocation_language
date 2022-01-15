from .alloc_lang_primitives import Node, Field, Percent

class Alloc(Node):
    def __init__(
        self, source: Field, value_node: Node, target: Field
    ):
        self.source = source
        self.value_node = value_node
        self.target = target

    def get_live_nodes(self, found=None):
        if (found is None):
            found = []
        return found + self.value_node.get_live_nodes()

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

    def evaluate_as_number(self, event_data: dict):
        source_val = float(self.source.evaluate(event_data))
        value = self.value_node.evaluate(event_data)

        quantity = min(source_val, value)

        return self.modify_data(event_data, quantity)

    def evaluate_as_share(self, event_data: dict):
        source_val = float(self.source.evaluate(event_data))
        value = self.value_node.evaluate(event_data)

        quantity = value * source_val

        return self.modify_data(event_data, quantity)

    def evaluate(self, event_data: dict) -> dict:
        
        if isinstance(self.value_node, Percent):
            return self.evaluate_as_share(event_data)

        return self.evaluate_as_number(event_data)