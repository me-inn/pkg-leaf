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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Status(Enum):
    """How far along this chapter is, which moves on its own and not with the book's."""

    APPROVED = "approved"
    DRAFT = "draft"
    REVIEW = "review"
    WRITING = "writing"


@dataclass
class Chapter:
    """One chapter of a book: its place in the running order and the text as it stands now.
    Earlier states of that text are revisions, each its own record.
    """
    book: str
    """The id of the book this chapter belongs to, in the system that holds the book."""

    title: str
    """The chapter heading."""

    content: Optional[str] = None
    """The text as it stands now. Empty while the chapter is only a heading."""

    created_at: Optional[datetime] = None
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    order: Optional[int] = None
    """Where it falls in the running order. The number the chapters are sorted by, not the
    number printed on the page.
    """
    status: Optional[Status] = None
    """How far along this chapter is, which moves on its own and not with the book's."""

    summary: Optional[str] = None
    """What happens in it, in a few lines. Written so the chapter can be reasoned about without
    reading it whole.
    """
    updated_at: Optional[datetime] = None
    word_count: Optional[int] = None
    """Words in the current text, counted by whoever holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'Chapter':
        assert isinstance(obj, dict)
        book = from_str(obj.get("book"))
        title = from_str(obj.get("title"))
        content = from_union([from_str, from_none], obj.get("content"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        order = from_union([from_int, from_none], obj.get("order"))
        status = from_union([Status, from_none], obj.get("status"))
        summary = from_union([from_str, from_none], obj.get("summary"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        word_count = from_union([from_int, from_none], obj.get("wordCount"))
        return Chapter(book, title, content, created_at, id, order, status, summary, updated_at, word_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["book"] = from_str(self.book)
        result["title"] = from_str(self.title)
        if self.content is not None:
            result["content"] = from_union([from_str, from_none], self.content)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.order is not None:
            result["order"] = from_union([from_int, from_none], self.order)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.summary is not None:
            result["summary"] = from_union([from_str, from_none], self.summary)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        if self.word_count is not None:
            result["wordCount"] = from_union([from_int, from_none], self.word_count)
        return result


def chapter_from_dict(s: Any) -> Chapter:
    return Chapter.from_dict(s)


def chapter_to_dict(x: Chapter) -> Any:
    return to_class(Chapter, x)