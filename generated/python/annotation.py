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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


class AnnotationType(Enum):
    """What kind of remark it is, which decides who it is addressed to: a todo waits on the
    author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
    at all.
    """
    AI_SUGGESTION = "ai_suggestion"
    BETA_FEEDBACK = "beta_feedback"
    NOTE = "note"
    QUESTION = "question"
    TODO = "todo"


@dataclass
class Annotation:
    """A note somebody left on a book, and where in the text they left it. The note is the
    record; the passage it points at stays in the chapter, quoted here only so the note still
    reads once the text around it has moved.
    """
    annotation_type: AnnotationType
    """What kind of remark it is, which decides who it is addressed to: a todo waits on the
    author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
    at all.
    """
    book: str
    """The id of the book it was left on, in the system that owns it."""

    note: str
    """What they wrote."""

    resolved: bool
    """Whether the note has been dealt with. It stays on the record once resolved; nothing here
    is removed by being answered.
    """
    anchor_end: Optional[int] = None
    """Where the passage ends, counted the same way."""

    anchor_start: Optional[int] = None
    """Where the passage starts in the chapter text, counted in characters from the beginning.
    Valid against the revision that was open at the time.
    """
    chapter: Optional[str] = None
    """The id of the chapter it was left on, in the system that owns it. Absent for a note about
    the book as a whole.
    """
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever left it. Absent for a note no person
    wrote.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    text_selection: Optional[str] = None
    """The passage as it read when the note was made. Kept verbatim because the anchors drift
    once the chapter is edited, and the quote is what survives that.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'Annotation':
        assert isinstance(obj, dict)
        annotation_type = AnnotationType(obj.get("annotationType"))
        book = from_str(obj.get("book"))
        note = from_str(obj.get("note"))
        resolved = from_bool(obj.get("resolved"))
        anchor_end = from_union([from_int, from_none], obj.get("anchorEnd"))
        anchor_start = from_union([from_int, from_none], obj.get("anchorStart"))
        chapter = from_union([from_str, from_none], obj.get("chapter"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        created_by = from_union([from_str, from_none], obj.get("createdBy"))
        id = from_union([from_str, from_none], obj.get("id"))
        text_selection = from_union([from_str, from_none], obj.get("textSelection"))
        return Annotation(annotation_type, book, note, resolved, anchor_end, anchor_start, chapter, created_at, created_by, id, text_selection)

    def to_dict(self) -> dict:
        result: dict = {}
        result["annotationType"] = to_enum(AnnotationType, self.annotation_type)
        result["book"] = from_str(self.book)
        result["note"] = from_str(self.note)
        result["resolved"] = from_bool(self.resolved)
        if self.anchor_end is not None:
            result["anchorEnd"] = from_union([from_int, from_none], self.anchor_end)
        if self.anchor_start is not None:
            result["anchorStart"] = from_union([from_int, from_none], self.anchor_start)
        if self.chapter is not None:
            result["chapter"] = from_union([from_str, from_none], self.chapter)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.created_by is not None:
            result["createdBy"] = from_union([from_str, from_none], self.created_by)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.text_selection is not None:
            result["textSelection"] = from_union([from_str, from_none], self.text_selection)
        return result


def annotation_from_dict(s: Any) -> Annotation:
    return Annotation.from_dict(s)


def annotation_to_dict(x: Annotation) -> Any:
    return to_class(Annotation, x)