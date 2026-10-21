# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class GenerationReady:
    """Content was written and is handed over in full. The one result that carries the work
    itself rather than a reference to it: the asking system has no database of generations to
    read it back from. Keys are snake_case, not the camelCase the rest of leaf uses: this
    travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
    owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
    follows the wire.
    """
    content_id: str
    """The generation that was made."""

    output: str
    """The text, as written."""

    session_id: str
    """The working session it was made in."""

    template: str
    """Which template it was written from."""

    overall_score: Optional[float] = None
    """What the pipeline thought of its own output. Absent when nothing scored it, which is not
    the same as a score of zero.
    """
    source_assets: Optional[List[str]] = None
    """The assets it was written from, by id."""

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationReady':
        assert isinstance(obj, dict)
        content_id = from_str(obj.get("content_id"))
        output = from_str(obj.get("output"))
        session_id = from_str(obj.get("session_id"))
        template = from_str(obj.get("template"))
        overall_score = from_union([from_float, from_none], obj.get("overall_score"))
        source_assets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("source_assets"))
        return GenerationReady(content_id, output, session_id, template, overall_score, source_assets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content_id"] = from_str(self.content_id)
        result["output"] = from_str(self.output)
        result["session_id"] = from_str(self.session_id)
        result["template"] = from_str(self.template)
        if self.overall_score is not None:
            result["overall_score"] = from_union([to_float, from_none], self.overall_score)
        if self.source_assets is not None:
            result["source_assets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_assets)
        return result


def generation_ready_from_dict(s: Any) -> GenerationReady:
    return GenerationReady.from_dict(s)


def generation_ready_to_dict(x: GenerationReady) -> Any:
    return to_class(GenerationReady, x)