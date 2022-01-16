from typing import Iterable
from alloc_lang_runtime.event_dataclasses import AssessmentEvent, EventData
from statistics import mean, median, mode

from ast_nodes.alloc_lang_primitives import AggField, Node


class AssessNode(Node):
    def __init__(self, agg_field_node: AggField):
        self.agg_field_node = agg_field_node

    def evaluate_stream(self, events: Iterable[EventData]):
        yield AssessmentEvent(
            self.agg_field_node.evaluate_stream(
                event for event in events if event.scope_flag
            )
        )

        yield from [event for event in events if not event.scope_flag]

    def evaluate(self, event: EventData) -> AssessmentEvent:
        if (not event.scope_flag):
            return event
        return AssessmentEvent(event.data[self.agg_field_node.name])
