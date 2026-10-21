# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AssetType(Enum):
    """Search only this kind of asset. Absent searches all of them.
    
    What kind of thing an asset is, which decides which pipeline reads it. A document covers
    an article, a PDF, or raw text.
    """
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"


class ResponseMode(Enum):
    """What to return: an answer grounded in the sources, or only the rewritten text, with
    nothing around it, for an editor that drops it straight into a document.
    """
    ANSWER = "answer"
    REWRITE = "rewrite"


@dataclass
class RagQueryRequested:
    """A question somebody wants answered out of what was put in. Carries the whole question,
    for the same reason repurpose does. Keys are snake_case, not the camelCase the rest of
    leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
    occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
    golden vectors. The shape follows the wire.
    """
    job_id: str
    """The job to report the answer against, created by the pipeline if it does not exist yet."""

    session_id: str
    """The working session to search in. The question is answered out of that session's
    material, not out of everything.
    """
    asset_type: Optional[AssetType] = None
    """Search only this kind of asset. Absent searches all of them."""

    language: Optional[str] = None
    """BCP-47 tag of the language to answer in. Detected from the question when absent."""

    query: Optional[str] = None
    """The question, in natural language. A blank one is not worked."""

    response_mode: Optional[ResponseMode] = None
    """What to return: an answer grounded in the sources, or only the rewritten text, with
    nothing around it, for an editor that drops it straight into a document.
    """
    top_k: Optional[int] = None
    """How many chunks to retrieve before answering. Absent leaves it to whoever searches."""

    @staticmethod
    def from_dict(obj: Any) -> 'RagQueryRequested':
        assert isinstance(obj, dict)
        job_id = from_str(obj.get("job_id"))
        session_id = from_str(obj.get("session_id"))
        asset_type = from_union([AssetType, from_none], obj.get("asset_type"))
        language = from_union([from_str, from_none], obj.get("language"))
        query = from_union([from_str, from_none], obj.get("query"))
        response_mode = from_union([ResponseMode, from_none], obj.get("response_mode"))
        top_k = from_union([from_int, from_none], obj.get("top_k"))
        return RagQueryRequested(job_id, session_id, asset_type, language, query, response_mode, top_k)

    def to_dict(self) -> dict:
        result: dict = {}
        result["job_id"] = from_str(self.job_id)
        result["session_id"] = from_str(self.session_id)
        if self.asset_type is not None:
            result["asset_type"] = from_union([lambda x: to_enum(AssetType, x), from_none], self.asset_type)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.query is not None:
            result["query"] = from_union([from_str, from_none], self.query)
        if self.response_mode is not None:
            result["response_mode"] = from_union([lambda x: to_enum(ResponseMode, x), from_none], self.response_mode)
        if self.top_k is not None:
            result["top_k"] = from_union([from_int, from_none], self.top_k)
        return result


def rag_query_requested_from_dict(s: Any) -> RagQueryRequested:
    return RagQueryRequested.from_dict(s)


def rag_query_requested_to_dict(x: RagQueryRequested) -> Any:
    return to_class(RagQueryRequested, x)