# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class RepurposeReady:
    """The shorter pieces were written and are handed over in full, for the same reason a
    generation is. Keys are snake_case, not the camelCase the rest of leaf uses: this travels
    inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
    owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
    follows the wire.
    """
    formats: Dict[str, str]
    """What came out, keyed by the format that was asked for — hooks, captions, and the rest. A
    format that was asked for and produced nothing is simply not here.
    """
    job_id: str
    """The job the work was done under, which is what the asker was waiting on."""

    session_id: str
    """The working session it was done in."""

    @staticmethod
    def from_dict(obj: Any) -> 'RepurposeReady':
        assert isinstance(obj, dict)
        formats = from_dict(from_str, obj.get("formats"))
        job_id = from_str(obj.get("job_id"))
        session_id = from_str(obj.get("session_id"))
        return RepurposeReady(formats, job_id, session_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["formats"] = from_dict(from_str, self.formats)
        result["job_id"] = from_str(self.job_id)
        result["session_id"] = from_str(self.session_id)
        return result


def repurpose_ready_from_dict(s: Any) -> RepurposeReady:
    return RepurposeReady.from_dict(s)


def repurpose_ready_to_dict(x: RepurposeReady) -> Any:
    return to_class(RepurposeReady, x)