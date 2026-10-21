# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


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


class AssetType(Enum):
    """What kind of thing it is, which decides which pipeline reads it.
    
    What kind of thing an asset is, which decides which pipeline reads it. A document covers
    an article, a PDF, or raw text.
    """
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"


class ProcessingStage(Enum):
    """Which step it was on. Read together with the status, it says where a run stopped: failed
    at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
    the first step runs.
    """
    AI_ENRICHMENT = "ai_enrichment"
    COMPLETED = "completed"
    EMBEDDING_INDEXING = "embedding_indexing"
    METADATA_EXTRACTION = "metadata_extraction"


class ProcessingStatus(Enum):
    """Where the pipeline stands on this asset.
    
    Where a pipeline stands on the thing it was given. Which move from which is a rule held
    beside the type, never in it.
    """
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"


class SourceType(Enum):
    """How it arrived: handed over as a file, or fetched from an address."""

    UPLOAD = "upload"
    URL = "url"


@dataclass
class StoredFile:
    """A preview image made from the asset. A second file the asset owns, not the asset itself:
    it is derived, and absent until something made one.
    
    Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
    store that holds it holds it, and this says which key to ask under and, while it lasts,
    where it can be fetched. Nothing is required, because a file can be known by its key
    before any address has been issued for it, and served by an address before anybody
    recorded a key.
    """
    size_bytes: Optional[int] = None
    """How big it is, so whoever is about to fetch it knows what they are asking for."""

    storage_key: Optional[str] = None
    """Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
    that store: a reader asks the store, never resolves the key itself.
    """
    url: Optional[str] = None
    """Where the file can be fetched right now. Often signed and short-lived, so it is read at
    the moment of use and never kept as the address of the file.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'StoredFile':
        assert isinstance(obj, dict)
        size_bytes = from_union([from_int, from_none], obj.get("sizeBytes"))
        storage_key = from_union([from_str, from_none], obj.get("storageKey"))
        url = from_union([from_str, from_none], obj.get("url"))
        return StoredFile(size_bytes, storage_key, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.size_bytes is not None:
            result["sizeBytes"] = from_union([from_int, from_none], self.size_bytes)
        if self.storage_key is not None:
            result["storageKey"] = from_union([from_str, from_none], self.storage_key)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Asset:
    """Something somebody put in — a file uploaded or a page ingested from a URL — and
    everything a machine later said about it. The bytes never travel: what travels is where
    they are kept, what kind of thing they are, and the reading a pipeline made of them.
    """
    asset_type: AssetType
    """What kind of thing it is, which decides which pipeline reads it."""

    content_type: str
    """The media type, as declared on arrival."""

    file_size: int
    """Size in bytes."""

    original_filename: str
    """The name the file had when it arrived. Never the name it is stored under."""

    processing_status: ProcessingStatus
    """Where the pipeline stands on this asset."""

    storage_key: str
    """Where the bytes sit in the store that holds them. Meaningful only to that store; a reader
    asks it, never resolves the key itself.
    """
    ai_description: Optional[str] = None
    """What a machine said the asset is."""

    ai_summary: Optional[str] = None
    """The longer reading a machine made of it."""

    ai_tags: Optional[List[str]] = None
    """Tags a machine put on it. Free text: the vocabulary belongs to whoever enriched the
    asset, not to this shape.
    """
    ai_title: Optional[str] = None
    """A title a machine gave it, which is not the filename and not a title a person wrote."""

    created_at: Optional[datetime] = None
    """When the asset was recorded, which is not when the file was made."""

    embedding: Optional[List[float]] = None
    """The semantic vector of the whole asset."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    metadata: Optional[Dict[str, Any]] = None
    """Raw technical metadata as the extractor read it off the file — dimensions, duration,
    codec, whatever the format carries.
    """
    owner: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever the asset belongs to. Absent for an
    asset that was put in before anybody claimed it.
    """
    processing_stage: Optional[ProcessingStage] = None
    """Which step it was on. Read together with the status, it says where a run stopped: failed
    at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
    the first step runs.
    """
    session: Optional[str] = None
    """The id of the working session it was put in during, in the system that owns the session.
    Absent when it was not put in through one.
    """
    source_type: Optional[SourceType] = None
    """How it arrived: handed over as a file, or fetched from an address."""

    source_url: Optional[str] = None
    """The address it was fetched from, when it was fetched. Kept even after ingestion, because
    the copy and the original drift apart.
    """
    thumbnail: Optional[StoredFile] = None
    """A preview image made from the asset. A second file the asset owns, not the asset itself:
    it is derived, and absent until something made one.
    """
    transcript_text: Optional[str] = None
    """What was said in it, for an asset that is heard rather than read."""

    updated_at: Optional[datetime] = None
    visual_summary: Optional[str] = None
    """What is seen in it, for an asset that is looked at rather than read."""

    @staticmethod
    def from_dict(obj: Any) -> 'Asset':
        assert isinstance(obj, dict)
        asset_type = AssetType(obj.get("assetType"))
        content_type = from_str(obj.get("contentType"))
        file_size = from_int(obj.get("fileSize"))
        original_filename = from_str(obj.get("originalFilename"))
        processing_status = ProcessingStatus(obj.get("processingStatus"))
        storage_key = from_str(obj.get("storageKey"))
        ai_description = from_union([from_str, from_none], obj.get("aiDescription"))
        ai_summary = from_union([from_str, from_none], obj.get("aiSummary"))
        ai_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("aiTags"))
        ai_title = from_union([from_str, from_none], obj.get("aiTitle"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        embedding = from_union([lambda x: from_list(from_float, x), from_none], obj.get("embedding"))
        id = from_union([from_str, from_none], obj.get("id"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        owner = from_union([from_str, from_none], obj.get("owner"))
        processing_stage = from_union([ProcessingStage, from_none], obj.get("processingStage"))
        session = from_union([from_str, from_none], obj.get("session"))
        source_type = from_union([SourceType, from_none], obj.get("sourceType"))
        source_url = from_union([from_str, from_none], obj.get("sourceUrl"))
        thumbnail = from_union([StoredFile.from_dict, from_none], obj.get("thumbnail"))
        transcript_text = from_union([from_str, from_none], obj.get("transcriptText"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        visual_summary = from_union([from_str, from_none], obj.get("visualSummary"))
        return Asset(asset_type, content_type, file_size, original_filename, processing_status, storage_key, ai_description, ai_summary, ai_tags, ai_title, created_at, embedding, id, metadata, owner, processing_stage, session, source_type, source_url, thumbnail, transcript_text, updated_at, visual_summary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["assetType"] = to_enum(AssetType, self.asset_type)
        result["contentType"] = from_str(self.content_type)
        result["fileSize"] = from_int(self.file_size)
        result["originalFilename"] = from_str(self.original_filename)
        result["processingStatus"] = to_enum(ProcessingStatus, self.processing_status)
        result["storageKey"] = from_str(self.storage_key)
        if self.ai_description is not None:
            result["aiDescription"] = from_union([from_str, from_none], self.ai_description)
        if self.ai_summary is not None:
            result["aiSummary"] = from_union([from_str, from_none], self.ai_summary)
        if self.ai_tags is not None:
            result["aiTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.ai_tags)
        if self.ai_title is not None:
            result["aiTitle"] = from_union([from_str, from_none], self.ai_title)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.embedding is not None:
            result["embedding"] = from_union([lambda x: from_list(to_float, x), from_none], self.embedding)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        if self.owner is not None:
            result["owner"] = from_union([from_str, from_none], self.owner)
        if self.processing_stage is not None:
            result["processingStage"] = from_union([lambda x: to_enum(ProcessingStage, x), from_none], self.processing_stage)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.source_type is not None:
            result["sourceType"] = from_union([lambda x: to_enum(SourceType, x), from_none], self.source_type)
        if self.source_url is not None:
            result["sourceUrl"] = from_union([from_str, from_none], self.source_url)
        if self.thumbnail is not None:
            result["thumbnail"] = from_union([lambda x: to_class(StoredFile, x), from_none], self.thumbnail)
        if self.transcript_text is not None:
            result["transcriptText"] = from_union([from_str, from_none], self.transcript_text)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        if self.visual_summary is not None:
            result["visualSummary"] = from_union([from_str, from_none], self.visual_summary)
        return result


def asset_from_dict(s: Any) -> Asset:
    return Asset.from_dict(s)


def asset_to_dict(x: Asset) -> Any:
    return to_class(Asset, x)