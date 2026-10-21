# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ValueSnapshot:
    """What something was worth over a stretch of time — a score, or a person saying yes or no
    to a generation. A reading taken, never a running total: two snapshots of the same thing
    are both true of their own window. Keys are snake_case, not the camelCase the rest of
    leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
    occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
    golden vectors. The shape follows the wire.
    """
    content_id: str
    """What was scored."""

    session_id: str
    """The working session it was taken in."""

    value: float
    """The reading, normalised. A thumb up is 1 and a thumb down is 0; what any other number
    means belongs to whoever took it.
    """
    window_end: datetime
    """End of the stretch the reading covers."""

    window_start: datetime
    """Start of the stretch the reading covers. Equal to the end for a reading of one moment,
    such as a thumb.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'ValueSnapshot':
        assert isinstance(obj, dict)
        content_id = from_str(obj.get("content_id"))
        session_id = from_str(obj.get("session_id"))
        value = from_float(obj.get("value"))
        window_end = from_datetime(obj.get("window_end"))
        window_start = from_datetime(obj.get("window_start"))
        return ValueSnapshot(content_id, session_id, value, window_end, window_start)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content_id"] = from_str(self.content_id)
        result["session_id"] = from_str(self.session_id)
        result["value"] = to_float(self.value)
        result["window_end"] = self.window_end.isoformat()
        result["window_start"] = self.window_start.isoformat()
        return result


def value_snapshot_from_dict(s: Any) -> ValueSnapshot:
    return ValueSnapshot.from_dict(s)


def value_snapshot_to_dict(x: ValueSnapshot) -> Any:
    return to_class(ValueSnapshot, x)