# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class FootnoteType(Enum):
    """What kind of note it is, which decides where it prints: at the foot of the page, at the
    back, inline, or in the list at the end.
    """
    BIBLIOGRAPHY = "bibliography"
    CITATION = "citation"
    ENDNOTE = "endnote"
    FOOTNOTE = "footnote"


@dataclass
class Footnote:
    """A note hanging off a point in a chapter's text — a footnote, an endnote, a citation, an
    entry in the bibliography. Its own record, because where it prints depends on the format
    the book is exported to and not on the sentence it came from.
    """
    chapter: str
    """The id of the chapter the note belongs to, in the system that holds the chapter."""

    content: str
    """What the note says."""

    anchor_position: Optional[int] = None
    """The offset into the chapter's text where the marker sits. Counted in characters from the
    start, so editing the text ahead of it moves the note.
    """
    created_at: Optional[datetime] = None
    footnote_type: Optional[FootnoteType] = None
    """What kind of note it is, which decides where it prints: at the foot of the page, at the
    back, inline, or in the list at the end.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    order: Optional[int] = None
    """Where it falls among that chapter's notes. What the printed marker is numbered from."""

    @staticmethod
    def from_dict(obj: Any) -> 'Footnote':
        assert isinstance(obj, dict)
        chapter = from_str(obj.get("chapter"))
        content = from_str(obj.get("content"))
        anchor_position = from_union([from_int, from_none], obj.get("anchorPosition"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        footnote_type = from_union([FootnoteType, from_none], obj.get("footnoteType"))
        id = from_union([from_str, from_none], obj.get("id"))
        order = from_union([from_int, from_none], obj.get("order"))
        return Footnote(chapter, content, anchor_position, created_at, footnote_type, id, order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chapter"] = from_str(self.chapter)
        result["content"] = from_str(self.content)
        if self.anchor_position is not None:
            result["anchorPosition"] = from_union([from_int, from_none], self.anchor_position)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.footnote_type is not None:
            result["footnoteType"] = from_union([lambda x: to_enum(FootnoteType, x), from_none], self.footnote_type)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.order is not None:
            result["order"] = from_union([from_int, from_none], self.order)
        return result


def footnote_from_dict(s: Any) -> Footnote:
    return Footnote.from_dict(s)


def footnote_to_dict(x: Footnote) -> Any:
    return to_class(Footnote, x)