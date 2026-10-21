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
class GenerationVariant:
    """A second take on a generation, asked for as its own piece of work. It says which
    generation it came from and which job was run for it — the text it produced belongs to
    that job's own record, not to this edge.
    """
    job: str
    """The processing job run to produce it, by its id in the system that runs it. The variant
    is the link between the two; neither side carries the other.
    """
    parent_generation: str
    """The generation this is a variant of, by its id in the system that holds it."""

    created_at: Optional[datetime] = None
    """When the variant was asked for, which is not when the job finished."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationVariant':
        assert isinstance(obj, dict)
        job = from_str(obj.get("job"))
        parent_generation = from_str(obj.get("parentGeneration"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        return GenerationVariant(job, parent_generation, created_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["job"] = from_str(self.job)
        result["parentGeneration"] = from_str(self.parent_generation)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


def generation_variant_from_dict(s: Any) -> GenerationVariant:
    return GenerationVariant.from_dict(s)


def generation_variant_to_dict(x: GenerationVariant) -> Any:
    return to_class(GenerationVariant, x)