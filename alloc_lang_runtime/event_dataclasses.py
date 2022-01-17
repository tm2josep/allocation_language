from dataclasses import dataclass

@dataclass
class EventData:
    data: dict
    scope_flag: bool = True

    def __str__(self):
        string_rep = "Current Scope: " + ("Y" if self.scope_flag else "N") + ", "
        for key, value in self.data.items():
            if (type(value) == int):
                string_rep += f"{key}: {value:,d}, "
            if (type(value) == float):
                string_rep += f"{key}: {value:,.2f}, "
            if (type(value) == str):
                string_rep += f"{key}: {value!r}, "
        return string_rep

@dataclass
class AssessmentEvent:
    final_value: float | str

    def __str__(self):
        if (type(self.final_value) == str):
            return f"Assessment: {self.final_value!r}"
        if (type(self.final_value) == float):
            return f"Assessment: {self.final_value:,.2f}"