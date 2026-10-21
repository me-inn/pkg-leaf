# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class PerformanceSignal:
    """One number a platform reported about one generated piece, at one moment. A reading and
    not a total: a second reading of the same metric is another record, so what a piece did
    over time is the series and never a field that gets overwritten.
    """
    generation: str
    """The id of the generated piece the number is about, in the system that owns it."""

    metric_name: str
    """What was counted, in the platform's own word for it. Free text for the same reason, and
    never translated on the way in: a platform's reach is not another platform's reach.
    """
    metric_value: float
    """The number, as reported. No unit travels with it — the unit is whatever the platform
    means by that metric name.
    """
    platform: str
    """Where the piece ran and who counted. Free text: the names belong to the platforms, and a
    list here would be out of date the week somebody publishes somewhere new.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    recorded_at: Optional[datetime] = None
    """When the reading was taken, which is not when the piece was published and not when the
    platform computed it.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'PerformanceSignal':
        assert isinstance(obj, dict)
        generation = from_str(obj.get("generation"))
        metric_name = from_str(obj.get("metricName"))
        metric_value = from_float(obj.get("metricValue"))
        platform = from_str(obj.get("platform"))
        id = from_union([from_str, from_none], obj.get("id"))
        recorded_at = from_union([from_datetime, from_none], obj.get("recordedAt"))
        return PerformanceSignal(generation, metric_name, metric_value, platform, id, recorded_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generation"] = from_str(self.generation)
        result["metricName"] = from_str(self.metric_name)
        result["metricValue"] = to_float(self.metric_value)
        result["platform"] = from_str(self.platform)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.recorded_at is not None:
            result["recordedAt"] = from_union([lambda x: x.isoformat(), from_none], self.recorded_at)
        return result


def performance_signal_from_dict(s: Any) -> PerformanceSignal:
    return PerformanceSignal.from_dict(s)


def performance_signal_to_dict(x: PerformanceSignal) -> Any:
    return to_class(PerformanceSignal, x)