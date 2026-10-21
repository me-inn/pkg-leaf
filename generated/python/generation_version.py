# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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
class GenerationVersion:
    """The text a generation held at one point in its life. Kept as its own record so editing a
    generation never loses what it said before — the generation carries the current text, the
    versions carry the ones it had.
    """
    generation: str
    """The generation this is a version of, by its id in the system that holds it."""

    output: str
    """The text as it stood in this version."""

    version: int
    """Which version this is, counting up within the generation. Ordering is the number's job;
    whether it may skip or repeat is the writing system's rule.
    """
    created_at: Optional[datetime] = None
    """When this version was written."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationVersion':
        assert isinstance(obj, dict)
        generation = from_str(obj.get("generation"))
        output = from_str(obj.get("output"))
        version = from_int(obj.get("version"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        return GenerationVersion(generation, output, version, created_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generation"] = from_str(self.generation)
        result["output"] = from_str(self.output)
        result["version"] = from_int(self.version)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


def generation_version_from_dict(s: Any) -> GenerationVersion:
    return GenerationVersion.from_dict(s)


def generation_version_to_dict(x: GenerationVersion) -> Any:
    return to_class(GenerationVersion, x)