from multiprocessing import Event
from typing import Iterable
from allocation_language.alloc_lang_data_containers.event_dataclasses import AssessmentEvent, EventData
from allocation_language.ast_nodes.alloc_lang_primitives import AggField, Field, Node

class AggregateNode(Node):
    def __init__(self, agg_field_nodes: Iterable[AggField]):
        self.agg_field_nodes = agg_field_nodes
    
    def evaluate_stream(self, events: Iterable[EventData]) -> Iterable[EventData]:
        remaining_events = []
        for event in events:
            if not isinstance(event, EventData):
                yield event
                continue
            
            if not event.scope_flag:
                yield event
                continue

            remaining_events.append(event)
        yield from self.aggregate_stream(remaining_events)
    
    def aggregate_stream(self, events: Iterable[EventData]):
        agg_data = {}
        for agg_node in self.agg_field_nodes:
            agg_data[agg_node.name] = agg_node.evaluate_stream(events)
        
        yield EventData(data=agg_data, scope_flag=True, aggregated=True)

class KeylessAggregateNode(AggregateNode):
    def __init__(self, agg_field_nodes: Iterable[AggField]):
        super().__init__(agg_field_nodes)


class KeyedAggregateNode(AggregateNode):
    def __init__(self, key_field: Field, agg_field_nodes: Iterable[AggField]):
        self.key_field = key_field
        super().__init__(agg_field_nodes)

    def aggregate_stream(self, events: Iterable[EventData]):
        keys = set(self.key_field.evaluate_stream(filter(lambda x: x.scope_flag, events)))
        for key in keys:
            yield from super().aggregate_stream(filter(lambda x: x.data[self.key.name] == key))