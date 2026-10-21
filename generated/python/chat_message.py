# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Role(Enum):
    """Who spoke. Two values: a person asks and the model answers, and nothing else writes a
    turn.
    """
    ASSISTANT = "assistant"
    USER = "user"


@dataclass
class RagSource:
    """One retrieved chunk an answer leaned on, as it was at the time of the answer. A pointer
    plus what a person needs to judge it — never the chunk, which stays with the asset it
    came from — so the citation still reads once the chunk has changed.
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
        asset_title = from_union([from_str, from_none], obj.get("assetTitle"))
        chunk_type = from_union([from_str, from_none], obj.get("chunkType"))
        excerpt = from_union([from_str, from_none], obj.get("excerpt"))
        score = from_union([from_float, from_none], obj.get("score"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        return RagSource(asset, chunk, asset_title, chunk_type, excerpt, score, thumbnail_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        result["chunk"] = from_str(self.chunk)
        if self.asset_title is not None:
            result["assetTitle"] = from_union([from_str, from_none], self.asset_title)
        if self.chunk_type is not None:
            result["chunkType"] = from_union([from_str, from_none], self.chunk_type)
        if self.excerpt is not None:
            result["excerpt"] = from_union([from_str, from_none], self.excerpt)
        if self.score is not None:
            result["score"] = from_union([to_float, from_none], self.score)
        if self.thumbnail_url is not None:
            result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        return result


@dataclass
class ChatMessage:
    """One turn of a conversation held against a library: what was asked, or what was answered,
    and for an answer the chunks it was grounded on. The sources are pointers with enough of
    the text to recognise them — never the chunk itself, which stays with the asset it came
    from.
    """
    content: str
    """What was said. The question as typed, or the answer as generated."""

    role: Role
    """Who spoke. Two values: a person asks and the model answers, and nothing else writes a
    turn.
    """
    created_at: Optional[datetime] = None
    """When the turn was recorded. The only ordering the conversation has."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The session the turn belongs to, as the system that owns the session names it. Absent on
    rows written before turns were scoped.
    """
    sources: Optional[List[RagSource]] = None
    """The chunks the answer was grounded on, in relevance order. Absent on a question, and
    empty on an answer that was grounded on nothing.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'ChatMessage':
        assert isinstance(obj, dict)
        content = from_str(obj.get("content"))
        role = Role(obj.get("role"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        sources = from_union([lambda x: from_list(RagSource.from_dict, x), from_none], obj.get("sources"))
        return ChatMessage(content, role, created_at, id, session, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_str(self.content)
        result["role"] = to_enum(Role, self.role)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.sources is not None:
            result["sources"] = from_union([lambda x: from_list(lambda x: to_class(RagSource, x), x), from_none], self.sources)
        return result


def chat_message_from_dict(s: Any) -> ChatMessage:
    return ChatMessage.from_dict(s)


def chat_message_to_dict(x: ChatMessage) -> Any:
    return to_class(ChatMessage, x)