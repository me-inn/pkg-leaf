# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Any, TypeVar, Callable, Type, cast
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ChunkType(Enum):
    """Which reading of the asset this piece is. They are indexed together but recall
    differently: title_tags catches a keyword, summary catches a meaning.
    """
    ARTICLE_TEXT = "article_text"
    DESCRIPTION = "description"
    METADATA = "metadata"
    SUMMARY = "summary"
    TITLE_TAGS = "title_tags"
    TRANSCRIPT = "transcript"
    VISUAL_SUMMARY = "visual_summary"


@dataclass
class AssetChunk:
    """One piece of an asset held separately so it can be searched on its own. The text is kept
    beside the vector so whoever answers from a chunk can show the excerpt it answered from,
    without opening the asset.
    """
    asset: str
    """The id of the asset this piece was cut from, in the system that owns it."""

    chunk_order: int
    """Position among the pieces of the same type on the same asset. Zero while a type yields
    one piece; it exists so splitting a long text later does not change the shape.
    """
    chunk_text: str
    """The text that was embedded, verbatim."""

    chunk_type: ChunkType
    """Which reading of the asset this piece is. They are indexed together but recall
    differently: title_tags catches a keyword, summary catches a meaning.
    """
    created_at: Optional[datetime] = None
    embedding: Optional[List[float]] = None
    """The semantic vector of this piece. A reader holding another model recomputes it from
    chunkText.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    metadata: Optional[Dict[str, Any]] = None
    """Whatever the splitter recorded about the cut — offsets into the source, token counts."""

    @staticmethod
    def from_dict(obj: Any) -> 'AssetChunk':
        assert isinstance(obj, dict)
        asset = from_str(obj.get("asset"))
        chunk_order = from_int(obj.get("chunkOrder"))
        chunk_text = from_str(obj.get("chunkText"))
        chunk_type = ChunkType(obj.get("chunkType"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        embedding = from_union([lambda x: from_list(from_float, x), from_none], obj.get("embedding"))
        id = from_union([from_str, from_none], obj.get("id"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        return AssetChunk(asset, chunk_order, chunk_text, chunk_type, created_at, embedding, id, metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        result["chunkOrder"] = from_int(self.chunk_order)
        result["chunkText"] = from_str(self.chunk_text)
        result["chunkType"] = to_enum(ChunkType, self.chunk_type)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.embedding is not None:
            result["embedding"] = from_union([lambda x: from_list(to_float, x), from_none], self.embedding)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        return result


def asset_chunk_from_dict(s: Any) -> AssetChunk:
    return AssetChunk.from_dict(s)


def asset_chunk_to_dict(x: AssetChunk) -> Any:
    return to_class(AssetChunk, x)