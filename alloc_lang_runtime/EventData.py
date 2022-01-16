from dataclasses import dataclass

@dataclass
class EventData:
    data: dict
    scope_flag = True