# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import List, Optional, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class DerivativeCreated:
    """Content was written from assets already put in. The relay understands this type natively,
    which is why it exists beside generation.ready: this one says a derivative was made, that
    one hands over what it says. Keys are snake_case, not the camelCase the rest of leaf
    uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
    event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
    vectors. The shape follows the wire.
    """
    content_id: str
    """The generation that was made."""

    session_id: str
    """The working session it was made in."""

    template: str
    """Which template it was written from. Free text: the templates belong to whoever generates."""

    source_assets: Optional[List[str]] = None
    """The assets it was written from, by id. Absent when nothing was drawn on."""

    @staticmethod
    def from_dict(obj: Any) -> 'DerivativeCreated':
        assert isinstance(obj, dict)
        content_id = from_str(obj.get("content_id"))
        session_id = from_str(obj.get("session_id"))
        template = from_str(obj.get("template"))
        source_assets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("source_assets"))
        return DerivativeCreated(content_id, session_id, template, source_assets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content_id"] = from_str(self.content_id)
        result["session_id"] = from_str(self.session_id)
        result["template"] = from_str(self.template)
        if self.source_assets is not None:
            result["source_assets"] = from_union([lambda x: from_list(from_str, x), from_none], self.source_assets)
        return result


def derivative_created_from_dict(s: Any) -> DerivativeCreated:
    return DerivativeCreated.from_dict(s)


def derivative_created_to_dict(x: DerivativeCreated) -> Any:
    return to_class(DerivativeCreated, x)