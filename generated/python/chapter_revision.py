# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ChapterRevision:
    """A chapter's text as it stood at one moment, kept whole rather than as a difference, so an
    old version reads without replaying the ones after it.
    """
    chapter: str
    """The id of the chapter this is a revision of, in the system that holds the chapter."""

    content: str
    """The whole text as it stood, not a difference against the one before."""

    version: int
    """Which revision of that chapter this is, counting up. Ordering comes from this and not
    from the clock, because two writes can land in the same second.
    """
    changed_by: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever made the change. Absent when it was
    made by software rather than a person.
    """
    change_summary: Optional[str] = None
    """One line on what changed, so a list of revisions can be read without opening each."""

    change_type: Optional[str] = None
    """What kind of change it was. Free text: the vocabulary belongs to the system that writes
    the revision.
    """
    created_at: Optional[datetime] = None
    """When the revision was written down."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    word_count: Optional[int] = None
    """Words in this revision's text."""

    @staticmethod
    def from_dict(obj: Any) -> 'ChapterRevision':
        assert isinstance(obj, dict)
        chapter = from_str(obj.get("chapter"))
        content = from_str(obj.get("content"))
        version = from_int(obj.get("version"))
        changed_by = from_union([from_str, from_none], obj.get("changedBy"))
        change_summary = from_union([from_str, from_none], obj.get("changeSummary"))
        change_type = from_union([from_str, from_none], obj.get("changeType"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        word_count = from_union([from_int, from_none], obj.get("wordCount"))
        return ChapterRevision(chapter, content, version, changed_by, change_summary, change_type, created_at, id, word_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chapter"] = from_str(self.chapter)
        result["content"] = from_str(self.content)
        result["version"] = from_int(self.version)
        if self.changed_by is not None:
            result["changedBy"] = from_union([from_str, from_none], self.changed_by)
        if self.change_summary is not None:
            result["changeSummary"] = from_union([from_str, from_none], self.change_summary)
        if self.change_type is not None:
            result["changeType"] = from_union([from_str, from_none], self.change_type)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.word_count is not None:
            result["wordCount"] = from_union([from_int, from_none], self.word_count)
        return result


def chapter_revision_from_dict(s: Any) -> ChapterRevision:
    return ChapterRevision.from_dict(s)


def chapter_revision_to_dict(x: ChapterRevision) -> Any:
    return to_class(ChapterRevision, x)