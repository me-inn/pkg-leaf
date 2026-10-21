# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class GenerationContextItem:
    """One piece of material that was put in front of the model for a generation, and where it
    came from. Written down because the source can change afterwards: this says what was
    actually read, in the order it was read.
    """
    content: str
    """The material as it was handed to the model. A copy on purpose — the source may be edited
    or deleted later, and this is what was read.
    """
    generation: str
    """The generation this was given to, by its id in the system that holds it."""

    rank: int
    """Its place in the order the items were assembled in, counting from the first. Position,
    not score.
    """
    source_id: str
    """The id of that thing, in the system that owns it. Paired with sourceType, which says what
    kind of id it is.
    """
    source_type: str
    """What kind of thing the material came from. Free text: the kinds belong to whatever the
    retrieving system can reach.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    similarity_score: Optional[float] = None
    """How close the retrieval judged it to the ask. Absent when the item was not chosen by
    similarity. The scale belongs to whichever retrieval produced it.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationContextItem':
        assert isinstance(obj, dict)
        content = from_str(obj.get("content"))
        generation = from_str(obj.get("generation"))
        rank = from_int(obj.get("rank"))
        source_id = from_str(obj.get("sourceId"))
        source_type = from_str(obj.get("sourceType"))
        id = from_union([from_str, from_none], obj.get("id"))
        similarity_score = from_union([from_float, from_none], obj.get("similarityScore"))
        return GenerationContextItem(content, generation, rank, source_id, source_type, id, similarity_score)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_str(self.content)
        result["generation"] = from_str(self.generation)
        result["rank"] = from_int(self.rank)
        result["sourceId"] = from_str(self.source_id)
        result["sourceType"] = from_str(self.source_type)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.similarity_score is not None:
            result["similarityScore"] = from_union([to_float, from_none], self.similarity_score)
        return result


def generation_context_item_from_dict(s: Any) -> GenerationContextItem:
    return GenerationContextItem.from_dict(s)


def generation_context_item_to_dict(x: GenerationContextItem) -> Any:
    return to_class(GenerationContextItem, x)