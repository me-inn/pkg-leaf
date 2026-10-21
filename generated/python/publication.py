# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Platform(Enum):
    """Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
    title's whereabouts stay complete.
    """
    AMAZON_KDP = "amazon_kdp"
    APPLE_BOOKS = "apple_books"
    GOOGLE_PLAY = "google_play"
    KOBO = "kobo"
    MANUAL = "manual"


class Status(Enum):
    """Where the listing stands on that store. Read from the store, not decided here."""

    DRAFT = "draft"
    LIVE = "live"
    REJECTED = "rejected"
    SUBMITTED = "submitted"
    UNPUBLISHED = "unpublished"


@dataclass
class Publication:
    """A book put out on one store, and what that store calls it. An edge between a title and a
    platform: the same book on three stores is three of these, each with its own listing, its
    own state and its own rate.
    """
    book: str
    """The id of the book being put out, in the system that holds the book."""

    platform: Platform
    """Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
    title's whereabouts stay complete.
    """
    created_at: Optional[datetime] = None
    estimated_monthly_royalty: Optional[float] = None
    """What this listing is expected to pay in a month, in the currency the store settles in. An
    estimate carried for planning, never an amount owed.
    """
    external_id: Optional[str] = None
    """What the store calls this listing — its ASIN, its product id. The only handle the store
    will answer to.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    listing_url: Optional[str] = None
    """The page a reader buys it on."""

    notes: Optional[str] = None
    """Anything about this listing worth writing down, in the words of whoever put it out."""

    published_at: Optional[datetime] = None
    """When the listing went live on the store."""

    royalty_rate: Optional[float] = None
    """The author's share, as a fraction: 0.7 is seventy per cent. A fraction and not a
    percentage so nobody has to guess which was meant.
    """
    status: Optional[Status] = None
    """Where the listing stands on that store. Read from the store, not decided here."""

    submitted_at: Optional[datetime] = None
    """When it was sent to the store, which is not when the store accepted it."""

    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Publication':
        assert isinstance(obj, dict)
        book = from_str(obj.get("book"))
        platform = Platform(obj.get("platform"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        estimated_monthly_royalty = from_union([from_float, from_none], obj.get("estimatedMonthlyRoyalty"))
        external_id = from_union([from_str, from_none], obj.get("externalId"))
        id = from_union([from_str, from_none], obj.get("id"))
        listing_url = from_union([from_str, from_none], obj.get("listingUrl"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        royalty_rate = from_union([from_float, from_none], obj.get("royaltyRate"))
        status = from_union([Status, from_none], obj.get("status"))
        submitted_at = from_union([from_datetime, from_none], obj.get("submittedAt"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return Publication(book, platform, created_at, estimated_monthly_royalty, external_id, id, listing_url, notes, published_at, royalty_rate, status, submitted_at, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["book"] = from_str(self.book)
        result["platform"] = to_enum(Platform, self.platform)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.estimated_monthly_royalty is not None:
            result["estimatedMonthlyRoyalty"] = from_union([to_float, from_none], self.estimated_monthly_royalty)
        if self.external_id is not None:
            result["externalId"] = from_union([from_str, from_none], self.external_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.listing_url is not None:
            result["listingUrl"] = from_union([from_str, from_none], self.listing_url)
        if self.notes is not None:
            result["notes"] = from_union([from_str, from_none], self.notes)
        if self.published_at is not None:
            result["publishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.published_at)
        if self.royalty_rate is not None:
            result["royaltyRate"] = from_union([to_float, from_none], self.royalty_rate)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.submitted_at is not None:
            result["submittedAt"] = from_union([lambda x: x.isoformat(), from_none], self.submitted_at)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def publication_from_dict(s: Any) -> Publication:
    return Publication.from_dict(s)


def publication_to_dict(x: Publication) -> Any:
    return to_class(Publication, x)