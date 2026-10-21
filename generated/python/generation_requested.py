# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class GenerationRequested:
    """A piece of content somebody wants written. What to write is in the job, not in the event.
    Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
    Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
    snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
    """
    job_id: str
    """The job holding the template, the sources and everything else the generation needs."""

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationRequested':
        assert isinstance(obj, dict)
        job_id = from_str(obj.get("job_id"))
        return GenerationRequested(job_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["job_id"] = from_str(self.job_id)
        return result


def generation_requested_from_dict(s: Any) -> GenerationRequested:
    return GenerationRequested.from_dict(s)


def generation_requested_to_dict(x: GenerationRequested) -> Any:
    return to_class(GenerationRequested, x)