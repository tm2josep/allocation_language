from dataclasses import dataclass

@dataclass
class EventData:
    data: dict
    scope_flag: bool = True

@dataclass
class AssessmentEvent:
    final_value: float | str