# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Notice:
    """A link somebody put out — a video, a magazine, a product — and one line about it. A
    pointer, never content: the system that holds the link holds what it says, and whoever
    carries the notice only says that the link exists and when.
    """
    by: str
    """The wallet, handle, or id under localIds of whoever put the link out."""

    url: str
    """Where the link goes. https, so a page vouching for it can hand it to a machine."""

    created_at: Optional[datetime] = None
    """When the notice was recorded, which is not when the link was published."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    line: Optional[str] = None
    """One line about it, in the words of whoever put it out. Read by a person; never fetched
    from the link.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'Notice':
        assert isinstance(obj, dict)
        by = from_str(obj.get("by"))
        url = from_str(obj.get("url"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        line = from_union([from_str, from_none], obj.get("line"))
        return Notice(by, url, created_at, id, line)

    def to_dict(self) -> dict:
        result: dict = {}
        result["by"] = from_str(self.by)
        result["url"] = from_str(self.url)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.line is not None:
            result["line"] = from_union([from_str, from_none], self.line)
        return result


def notice_from_dict(s: Any) -> Notice:
    return Notice.from_dict(s)


def notice_to_dict(x: Notice) -> Any:
    return to_class(Notice, x)