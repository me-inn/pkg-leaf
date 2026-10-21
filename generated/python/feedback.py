# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Feedback:
    """A rating somebody gave a thing the software produced, with a line about it if they wrote
    one. About an output and not about a person: it carries no subject, no consent and no
    signature, which is what separates it from a testimony.
    """
    rating: int
    """The rating as given, 1 to 5. Collected both ways: as a thumb, where only 1 and 5 are ever
    written, and as the whole scale. Which of the two it was is not recorded, so a mean over
    mixed records is a number about nothing.
    """
    target: str
    """The id of that thing, in the system that owns it. It is read together with targetType and
    alone means nothing — two kinds of target do not share an id space.
    """
    target_type: str
    """What kind of thing was rated. Free text with the two the system records so far: a target
    type is added whenever something new becomes ratable, and a closed list here would have
    to be versioned for each one.
    """
    comment: Optional[str] = None
    """What they wrote alongside the rating, in their own words."""

    created_at: Optional[datetime] = None
    """When it was given."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The id of the working session it came from, in the system that holds it. Not a person."""

    @staticmethod
    def from_dict(obj: Any) -> 'Feedback':
        assert isinstance(obj, dict)
        rating = from_int(obj.get("rating"))
        target = from_str(obj.get("target"))
        target_type = from_str(obj.get("targetType"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        return Feedback(rating, target, target_type, comment, created_at, id, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rating"] = from_int(self.rating)
        result["target"] = from_str(self.target)
        result["targetType"] = from_str(self.target_type)
        if self.comment is not None:
            result["comment"] = from_union([from_str, from_none], self.comment)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def feedback_from_dict(s: Any) -> Feedback:
    return Feedback.from_dict(s)


def feedback_to_dict(x: Feedback) -> Any:
    return to_class(Feedback, x)