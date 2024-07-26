from datetime import timedelta
from enum import Enum, auto


class StrEnum(str, Enum):
    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values) -> str:  # type: ignore
        """
        Uses the name as the automatic value, rather than an integer

        See https://docs.python.org/3/library/enum.html#using-automatic-values for reference
        """
        return name


class Period(StrEnum):
    SECONDS = auto()
    MINUTES = auto()
    HOURS = auto()
    DAYS = auto()
    WEEKS = auto()

    def to_seconds(self) -> timedelta:
        seconds = {
            Period.SECONDS: 1,
            Period.MINUTES: 60,
            Period.HOURS: 60 * 60,
            Period.DAYS: 60 * 60 * 24,
            Period.WEEKS: 60 * 60 * 24 * 7
        }[self]

        return timedelta(seconds=seconds)
