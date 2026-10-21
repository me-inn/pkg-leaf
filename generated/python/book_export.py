# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from enum import Enum
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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class StoredFile:
    """The rendered file, where it is kept and how big it is. Absent until the rendering says
    done.
    
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


class Format(Enum):
    """What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
    not one: the page, the bleed and the margins differ.
    """
    DOCX = "docx"
    EPUB = "epub"
    PDF_EBOOK = "pdf_ebook"
    PDF_PRINT = "pdf_print"


class Status(Enum):
    """How the rendering went. The file is only there to fetch once this says done."""

    DONE = "done"
    FAILED = "failed"
    PROCESSING = "processing"
    QUEUED = "queued"


@dataclass
class BookExport:
    """One rendering of a book into a file somebody can hand over — a pdf, an epub, a docx. A
    pointer and a state, never the file: the bytes live in the store that rendered them, and
    this says which store, under which key, and whether it finished.
    """
    book: str
    """The id of the book that was rendered, in the system that holds the book."""

    format: Format
    """What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
    not one: the page, the bleed and the margins differ.
    """
    completed_at: Optional[datetime] = None
    """When the rendering finished, whether it succeeded or failed."""

    created_at: Optional[datetime] = None
    """When the export was asked for, which is not when the file was ready."""

    error_message: Optional[str] = None
    """Why the rendering failed, in the words of whoever rendered it. Present only when it did."""

    file: Optional[StoredFile] = None
    """The rendered file, where it is kept and how big it is. Absent until the rendering says
    done.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    status: Optional[Status] = None
    """How the rendering went. The file is only there to fetch once this says done."""

    @staticmethod
    def from_dict(obj: Any) -> 'BookExport':
        assert isinstance(obj, dict)
        book = from_str(obj.get("book"))
        format = Format(obj.get("format"))
        completed_at = from_union([from_datetime, from_none], obj.get("completedAt"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        error_message = from_union([from_str, from_none], obj.get("errorMessage"))
        file = from_union([StoredFile.from_dict, from_none], obj.get("file"))
        id = from_union([from_str, from_none], obj.get("id"))
        status = from_union([Status, from_none], obj.get("status"))
        return BookExport(book, format, completed_at, created_at, error_message, file, id, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["book"] = from_str(self.book)
        result["format"] = to_enum(Format, self.format)
        if self.completed_at is not None:
            result["completedAt"] = from_union([lambda x: x.isoformat(), from_none], self.completed_at)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.error_message is not None:
            result["errorMessage"] = from_union([from_str, from_none], self.error_message)
        if self.file is not None:
            result["file"] = from_union([lambda x: to_class(StoredFile, x), from_none], self.file)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        return result


def book_export_from_dict(s: Any) -> BookExport:
    return BookExport.from_dict(s)


def book_export_to_dict(x: BookExport) -> Any:
    return to_class(BookExport, x)