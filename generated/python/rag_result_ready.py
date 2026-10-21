# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class RagSource:
    """One chunk the answer stood on. The same shape as common.v1 ragSource, written out here in
    the relay's snake_case rather than referenced.
    """
    asset: str
    """The asset the chunk came from, as the system that owns the asset names it."""

    chunk: str
    """The chunk itself, as the system that owns the chunk names it."""

    asset_title: Optional[str] = None
    """What the parent asset was called when the answer was written. Kept as a copy on purpose:
    a citation should still read after the asset is retitled.
    """
    chunk_type: Optional[str] = None
    """Which part of the asset the chunk is — a summary, a transcript, a block of article text.
    Free text: the vocabulary belongs to whoever chunks.
    """
    excerpt: Optional[str] = None
    """The opening of the chunk, carried so a person can see what was cited without fetching it."""

    score: Optional[float] = None
    """How close the chunk sat to the question, as the retrieval scored it. Comparable inside
    one search, not across searches: the scale belongs to the model that searched.
    """
    thumbnail_url: Optional[str] = None
    """A picture of the parent asset, when the system that serves it offers one. Derived, and
    resolvable only against the deploy that built it.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'RagSource':
        assert isinstance(obj, dict)
        asset = from_str(obj.get("asset"))
        chunk = from_str(obj.get("chunk"))
        asset_title = from_union([from_str, from_none], obj.get("asset_title"))
        chunk_type = from_union([from_str, from_none], obj.get("chunk_type"))
        excerpt = from_union([from_str, from_none], obj.get("excerpt"))
        score = from_union([from_float, from_none], obj.get("score"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnail_url"))
        return RagSource(asset, chunk, asset_title, chunk_type, excerpt, score, thumbnail_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        result["chunk"] = from_str(self.chunk)
        if self.asset_title is not None:
            result["asset_title"] = from_union([from_str, from_none], self.asset_title)
        if self.chunk_type is not None:
            result["chunk_type"] = from_union([from_str, from_none], self.chunk_type)
        if self.excerpt is not None:
            result["excerpt"] = from_union([from_str, from_none], self.excerpt)
        if self.score is not None:
            result["score"] = from_union([to_float, from_none], self.score)
        if self.thumbnail_url is not None:
            result["thumbnail_url"] = from_union([from_str, from_none], self.thumbnail_url)
        return result


@dataclass
class RagResultReady:
    """A question was answered, and the answer comes back with what it was built out of. The
    sources travel so the asker can show its work without holding the chunks. Keys are
    snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
    envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
    snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
    """
    answer: str
    """The answer, grounded in the sources below."""

    query: str
    """The question as asked, repeated so the answer is readable on its own."""

    session_id: str
    """The working session the question was asked in."""

    job_id: Optional[str] = None
    """The job the answer was worked under, when the question arrived as one."""

    sources: Optional[List[RagSource]] = None
    """The chunks the answer was built from, in order of relevance. Absent when the search found
    nothing to stand on. A producer of this event always fills in score, chunkType and
    excerpt, even though the shared shape only insists on the two pointers.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'RagResultReady':
        assert isinstance(obj, dict)
        answer = from_str(obj.get("answer"))
        query = from_str(obj.get("query"))
        session_id = from_str(obj.get("session_id"))
        job_id = from_union([from_str, from_none], obj.get("job_id"))
        sources = from_union([lambda x: from_list(RagSource.from_dict, x), from_none], obj.get("sources"))
        return RagResultReady(answer, query, session_id, job_id, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        result["answer"] = from_str(self.answer)
        result["query"] = from_str(self.query)
        result["session_id"] = from_str(self.session_id)
        if self.job_id is not None:
            result["job_id"] = from_union([from_str, from_none], self.job_id)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(lambda x: to_class(RagSource, x), x), from_none], self.sources)
        return result


def rag_result_ready_from_dict(s: Any) -> RagResultReady:
    return RagResultReady.from_dict(s)


def rag_result_ready_to_dict(x: RagResultReady) -> Any:
    return to_class(RagResultReady, x)