from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self
