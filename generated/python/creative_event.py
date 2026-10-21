# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class EventType(Enum):
    """What happened, written as <domain>.<action>. The requested forms are commands addressed
    to the pipeline; the rest are results it emits. It alone decides which payload shape
    applies — two different commands can carry the same single id and are told apart by
    nothing else.
    """
    ASSET_EDIT_READY = "asset.edit_ready"
    ASSET_EDIT_REQUESTED = "asset.edit_requested"
    ASSET_INGEST_REQUESTED = "asset.ingest_requested"
    ASSET_URL_INGEST_REQUESTED = "asset.url_ingest_requested"
    CITATION_CREATED = "citation.created"
    DERIVATIVE_CREATED = "derivative.created"
    GENERATION_READY = "generation.ready"
    GENERATION_REQUESTED = "generation.requested"
    RAG_QUERY_REQUESTED = "rag.query_requested"
    RAG_RESULT_READY = "rag.result_ready"
    READ_COMPLETED = "read.completed"
    REPURPOSE_READY = "repurpose.ready"
    REPURPOSE_REQUESTED = "repurpose.requested"
    SIGNAL_ERROR = "signal.error"
    VALUE_SNAPSHOT = "value.snapshot"


@dataclass
class CreativeEvent:
    """One thing the creative pipeline was asked to do, or one thing it finished — as it travels
    between the system that asks and the system that works. Commands go one way and results
    come back the other way over the same relay, so they are one shape with one type field
    rather than two. The event carries no content: what it carries is an id of something a
    system already holds, and enough words to act on it. Keys are snake_case, not the
    camelCase the rest of leaf uses: this travels inside a Liquid envelope, whose own fields
    (event_id, occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact
    by signed golden vectors. The shape follows the wire.
    """
    event_type: EventType
    """What happened, written as <domain>.<action>. The requested forms are commands addressed
    to the pipeline; the rest are results it emits. It alone decides which payload shape
    applies — two different commands can carry the same single id and are told apart by
    nothing else.
    """
    payload: Dict[str, Any]
    """What the event is about. Open on purpose: eventType decides which schema the payload is,
    and a reader picks that type rather than matching on the shape. The union used to live
    here as anyOf and the generator kept only its first branch, so the other fourteen
    payloads had no type at all; each is now its own schema. asset.ingest_requested ->
    AssetIngestRequested; asset.url_ingest_requested -> AssetUrlIngestRequested;
    generation.requested -> GenerationRequested; repurpose.requested -> RepurposeRequested;
    rag.query_requested -> RagQueryRequested; asset.edit_requested -> AssetEditRequested;
    read.completed -> ReadCompleted; derivative.created -> DerivativeCreated;
    citation.created -> CitationCreated; value.snapshot -> ValueSnapshot; signal.error ->
    SignalError; generation.ready -> GenerationReady; rag.result_ready -> RagResultReady;
    repurpose.ready -> RepurposeReady; asset.edit_ready -> AssetEditReady.
    """
    author: Optional[str] = None
    """ed25519 public key, hex, of whoever signed the event. The only thing that says who asked:
    a reader admits an event by this key, never by the name below.
    """
    author_name: Optional[str] = None
    """What the signing system calls itself, such as creativeflow. A label for reading a log; it
    proves nothing, and two systems may well claim the same one.
    """
    content_id: Optional[str] = None
    """The asset, generation or job the event is about, repeated outside the payload so a reader
    can file the event without opening it. Absent for events about no single thing, such as
    an error.
    """
    device_id: Optional[str] = None
    """The device the event was written on, when more than one writes for the same author."""

    id: Optional[str] = None
    """The record's own id in the system that holds it. Also what makes the event replayable
    without doing the work twice: a reader that has seen this id has already acted.
    """
    lamport: Optional[int] = None
    """A counter for ordering events from one author when wall clocks disagree. Comparable only
    against events from the same author.
    """
    occurred_at: Optional[datetime] = None
    """When the author says it happened, which is not when a reader received it."""

    owner_unit_ref: Optional[str] = None
    """The session or unit the event belongs to, which is who answers for it. Set on errors
    above all, where it is the only thing saying whose work broke.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'CreativeEvent':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        payload = from_dict(lambda x: x, obj.get("payload"))
        author = from_union([from_str, from_none], obj.get("author"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        content_id = from_union([from_str, from_none], obj.get("content_id"))
        device_id = from_union([from_str, from_none], obj.get("device_id"))
        id = from_union([from_str, from_none], obj.get("id"))
        lamport = from_union([from_int, from_none], obj.get("lamport"))
        occurred_at = from_union([from_datetime, from_none], obj.get("occurred_at"))
        owner_unit_ref = from_union([from_str, from_none], obj.get("owner_unit_ref"))
        return CreativeEvent(event_type, payload, author, author_name, content_id, device_id, id, lamport, occurred_at, owner_unit_ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["payload"] = from_dict(lambda x: x, self.payload)
        if self.author is not None:
            result["author"] = from_union([from_str, from_none], self.author)
        if self.author_name is not None:
            result["author_name"] = from_union([from_str, from_none], self.author_name)
        if self.content_id is not None:
            result["content_id"] = from_union([from_str, from_none], self.content_id)
        if self.device_id is not None:
            result["device_id"] = from_union([from_str, from_none], self.device_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.lamport is not None:
            result["lamport"] = from_union([from_int, from_none], self.lamport)
        if self.occurred_at is not None:
            result["occurred_at"] = from_union([lambda x: x.isoformat(), from_none], self.occurred_at)
        if self.owner_unit_ref is not None:
            result["owner_unit_ref"] = from_union([from_str, from_none], self.owner_unit_ref)
        return result


def creative_event_from_dict(s: Any) -> CreativeEvent:
    return CreativeEvent.from_dict(s)


def creative_event_to_dict(x: CreativeEvent) -> Any:
    return to_class(CreativeEvent, x)