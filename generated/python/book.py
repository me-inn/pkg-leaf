# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class StoredFile:
    """The cover image, where it is kept. Absent while the title has none.
    
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


class Genre(Enum):
    """The shelf it belongs on. A closed list because it decides how the title is filed, not how
    it reads.
    """
    ACADEMIC = "academic"
    BIOGRAPHY = "biography"
    BUSINESS = "business"
    CHILDREN = "children"
    FANTASY = "fantasy"
    FICTION = "fiction"
    HISTORICAL = "historical"
    HORROR = "horror"
    NON_FICTION = "non_fiction"
    OTHER = "other"
    POETRY = "poetry"
    ROMANCE = "romance"
    SCIENCE_FICTION = "science_fiction"
    SELF_HELP = "self_help"
    THRILLER = "thriller"
    YOUNG_ADULT = "young_adult"


class Status(Enum):
    """How far along it is. Which move from which is a rule held beside the type, never in it."""

    APPROVED = "approved"
    DRAFT = "draft"
    PUBLISHED = "published"
    REVIEW = "review"
    WRITING = "writing"


@dataclass
class Book:
    """A long-form title somebody is writing: what it is about, how far along it is, and where
    its cover sits. The chapters are not inside it — each is its own record pointing back, so
    a book can be read without carrying its whole text.
    """
    genre: Genre
    """The shelf it belongs on. A closed list because it decides how the title is filed, not how
    it reads.
    """
    title: str
    """The title on the cover."""

    ai_model: Optional[str] = None
    """The model that helped write it, named as the system that called it names it. Absent when
    nothing was asked of one.
    """
    author: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever is writing it. Absent while the title
    belongs to nobody yet.
    """
    cover: Optional[StoredFile] = None
    """The cover image, where it is kept. Absent while the title has none."""

    cover_prompt: Optional[str] = None
    """The brief the cover image was asked for with. Kept because the image can be asked for
    again.
    """
    created_at: Optional[datetime] = None
    current_word_count: Optional[int] = None
    """Words written so far across the chapters. Counted by whoever holds the text, carried here
    so a reader of the book alone can say how far along it is.
    """
    description: Optional[str] = None
    """What the book is about, in the words of whoever is writing it. Written for a reader
    deciding, not for a catalogue.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    kdp_bisac: Optional[str] = None
    """The BISAC subject code given to the store, such as FIC000000. Separate from genre: one is
    ours, this one is the trade's.
    """
    kdp_keywords: Optional[List[str]] = None
    """The keywords the title is listed under on the store. Free text, in the words of whoever
    sells it.
    """
    language: Optional[str] = None
    """The language the book is written in, as a BCP 47 tag such as pt, en or pt-BR."""

    session: Optional[str] = None
    """The id of the working session the book was started from, in the system that holds that
    session. Absent when it was not started from one.
    """
    status: Optional[Status] = None
    """How far along it is. Which move from which is a rule held beside the type, never in it."""

    subtitle: Optional[str] = None
    """The line under the title, when there is one."""

    target_word_count: Optional[int] = None
    """The length being aimed at, set by whoever is writing. Zero while no target was chosen."""

    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Book':
        assert isinstance(obj, dict)
        genre = Genre(obj.get("genre"))
        title = from_str(obj.get("title"))
        ai_model = from_union([from_str, from_none], obj.get("aiModel"))
        author = from_union([from_str, from_none], obj.get("author"))
        cover = from_union([StoredFile.from_dict, from_none], obj.get("cover"))
        cover_prompt = from_union([from_str, from_none], obj.get("coverPrompt"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        current_word_count = from_union([from_int, from_none], obj.get("currentWordCount"))
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_str, from_none], obj.get("id"))
        kdp_bisac = from_union([from_str, from_none], obj.get("kdpBisac"))
        kdp_keywords = from_union([lambda x: from_list(from_str, x), from_none], obj.get("kdpKeywords"))
        language = from_union([from_str, from_none], obj.get("language"))
        session = from_union([from_str, from_none], obj.get("session"))
        status = from_union([Status, from_none], obj.get("status"))
        subtitle = from_union([from_str, from_none], obj.get("subtitle"))
        target_word_count = from_union([from_int, from_none], obj.get("targetWordCount"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return Book(genre, title, ai_model, author, cover, cover_prompt, created_at, current_word_count, description, id, kdp_bisac, kdp_keywords, language, session, status, subtitle, target_word_count, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["genre"] = to_enum(Genre, self.genre)
        result["title"] = from_str(self.title)
        if self.ai_model is not None:
            result["aiModel"] = from_union([from_str, from_none], self.ai_model)
        if self.author is not None:
            result["author"] = from_union([from_str, from_none], self.author)
        if self.cover is not None:
            result["cover"] = from_union([lambda x: to_class(StoredFile, x), from_none], self.cover)
        if self.cover_prompt is not None:
            result["coverPrompt"] = from_union([from_str, from_none], self.cover_prompt)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.current_word_count is not None:
            result["currentWordCount"] = from_union([from_int, from_none], self.current_word_count)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.kdp_bisac is not None:
            result["kdpBisac"] = from_union([from_str, from_none], self.kdp_bisac)
        if self.kdp_keywords is not None:
            result["kdpKeywords"] = from_union([lambda x: from_list(from_str, x), from_none], self.kdp_keywords)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.subtitle is not None:
            result["subtitle"] = from_union([from_str, from_none], self.subtitle)
        if self.target_word_count is not None:
            result["targetWordCount"] = from_union([from_int, from_none], self.target_word_count)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def book_from_dict(s: Any) -> Book:
    return Book.from_dict(s)


def book_to_dict(x: Book) -> Any:
    return to_class(Book, x)