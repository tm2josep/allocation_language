from typing import Iterable
from alloc_lang_runtime.event_dataclasses import EventData
from ast_nodes.alloc_lang_primitives import Node
from ast_nodes.alloc_lang_scope import Condition


class DiscardNode(Node):
    def __init__(self, condition: Condition):
        self.condition = condition

    def evaluate_stream(self, events: Iterable[EventData]) -> Iterable[EventData]:
        for event in events:
            if self.condition.evaluate(event):
                yield event

    def evaluate(self, event: EventData) -> EventData | None:
        if self.condition(event):
            return event

        return None
