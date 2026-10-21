# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class BrandVoice:
    """A snapshot of what a session has been approving: how much, how well it scored, and which
    channels and objectives it kept coming back to. Counted once and written down, so the
    figures a person saw on a day can be shown again on another day without recounting them.
    """
    approved_count: int
    """How many pieces had been approved when the snapshot was taken."""

    avg_overall_score: Optional[float] = None
    """The mean of the latest score of each scored generation. Absent when nothing had been
    scored yet, which is not the same as zero.
    """
    created_at: Optional[datetime] = None
    """When the snapshot was taken. It is what makes the figures readable later: they are true
    of that moment and of no other.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The session this was counted over, as the system that owns the session names it.
    Optional: scoping a profile to a working session is how Creative Flow holds it, not part
    of what it is, and a system without sessions must be able to carry the same shape.
    """
    top_channels: Optional[List[str]] = None
    """The channels that came up most, most frequent first. A list, whatever a given store
    serialises it into.
    """
    top_objectives: Optional[List[str]] = None
    """The objectives that came up most, most frequent first."""

    @staticmethod
    def from_dict(obj: Any) -> 'BrandVoice':
        assert isinstance(obj, dict)
        approved_count = from_int(obj.get("approvedCount"))
        avg_overall_score = from_union([from_float, from_none], obj.get("avgOverallScore"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        top_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("topChannels"))
        top_objectives = from_union([lambda x: from_list(from_str, x), from_none], obj.get("topObjectives"))
        return BrandVoice(approved_count, avg_overall_score, created_at, id, session, top_channels, top_objectives)

    def to_dict(self) -> dict:
        result: dict = {}
        result["approvedCount"] = from_int(self.approved_count)
        if self.avg_overall_score is not None:
            result["avgOverallScore"] = from_union([to_float, from_none], self.avg_overall_score)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.top_channels is not None:
            result["topChannels"] = from_union([lambda x: from_list(from_str, x), from_none], self.top_channels)
        if self.top_objectives is not None:
            result["topObjectives"] = from_union([lambda x: from_list(from_str, x), from_none], self.top_objectives)
        return result


def brand_voice_from_dict(s: Any) -> BrandVoice:
    return BrandVoice.from_dict(s)


def brand_voice_to_dict(x: BrandVoice) -> Any:
    return to_class(BrandVoice, x)