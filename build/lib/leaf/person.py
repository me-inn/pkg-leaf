# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Type, Callable, cast
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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Locale(Enum):
    """The language to write to this point in."""

    EN = "en"
    ES = "es"
    PT = "pt"


class TypeEnum(Enum):
    """Which channel the value is for."""

    EMAIL = "email"
    MOBILE = "mobile"
    PHONE = "phone"
    WHATSAPP = "whatsapp"


@dataclass
class ContactPoint:
    """One way to reach an actor."""

    type: TypeEnum
    """Which channel the value is for."""

    value: str
    """An address, or a number in E.164 digits including the country code."""

    locale: Optional[Locale] = None
    """The language to write to this point in."""

    verified: Optional[bool] = None
    verified_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContactPoint':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        value = from_str(obj.get("value"))
        locale = from_union([Locale, from_none], obj.get("locale"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        verified_at = from_union([from_datetime, from_none], obj.get("verifiedAt"))
        return ContactPoint(type, value, locale, verified, verified_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["value"] = from_str(self.value)
        if self.locale is not None:
            result["locale"] = from_union([lambda x: to_enum(Locale, x), from_none], self.locale)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.verified_at is not None:
            result["verifiedAt"] = from_union([lambda x: x.isoformat(), from_none], self.verified_at)
        return result


@dataclass
class TaxIdentifier:
    """A tax or registry identifier."""

    type: str
    """The scheme, such as CNPJ, CPF, NIF, VAT or EIN. Free text, always stated, never inferred
    from the length of the value.
    """
    value: str
    country: Optional[str] = None
    """ISO 3166-1 alpha-2, when the scheme does not imply one."""

    document_url: Optional[str] = None
    """URL of the supporting document."""

    @staticmethod
    def from_dict(obj: Any) -> 'TaxIdentifier':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        value = from_str(obj.get("value"))
        country = from_union([from_str, from_none], obj.get("country"))
        document_url = from_union([from_str, from_none], obj.get("documentUrl"))
        return TaxIdentifier(type, value, country, document_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["value"] = from_str(self.value)
        if self.country is not None:
            result["country"] = from_union([from_str, from_none], self.country)
        if self.document_url is not None:
            result["documentUrl"] = from_union([from_str, from_none], self.document_url)
        return result


@dataclass
class Person:
    """A person. Holds no authentication secret: password hashes, reset tokens and auth
    providers belong to the system that authenticates.
    """
    display_name: str
    """The name they are known by."""

    contacts: Optional[List[ContactPoint]] = None
    """Ways to reach them."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2, where they are registered."""

    created_at: Optional[datetime] = None
    handle: Optional[str] = None
    """Their public address, without the @."""

    locale: Optional[Locale] = None
    local_ids: Optional[Dict[str, str]] = None
    """The id this person has in each system that holds a record of them."""

    tax_ids: Optional[List[TaxIdentifier]] = None
    """Their tax or registry identifiers, one per scheme."""

    wallet: Optional[str] = None
    """ed25519 public key, hex. Identifies the person. Absent until they hold one."""

    @staticmethod
    def from_dict(obj: Any) -> 'Person':
        assert isinstance(obj, dict)
        display_name = from_str(obj.get("displayName"))
        contacts = from_union([lambda x: from_list(ContactPoint.from_dict, x), from_none], obj.get("contacts"))
        country = from_union([from_str, from_none], obj.get("country"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        locale = from_union([Locale, from_none], obj.get("locale"))
        local_ids = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("localIds"))
        tax_ids = from_union([lambda x: from_list(TaxIdentifier.from_dict, x), from_none], obj.get("taxIds"))
        wallet = from_union([from_str, from_none], obj.get("wallet"))
        return Person(display_name, contacts, country, created_at, handle, locale, local_ids, tax_ids, wallet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["displayName"] = from_str(self.display_name)
        if self.contacts is not None:
            result["contacts"] = from_union([lambda x: from_list(lambda x: to_class(ContactPoint, x), x), from_none], self.contacts)
        if self.country is not None:
            result["country"] = from_union([from_str, from_none], self.country)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.handle is not None:
            result["handle"] = from_union([from_str, from_none], self.handle)
        if self.locale is not None:
            result["locale"] = from_union([lambda x: to_enum(Locale, x), from_none], self.locale)
        if self.local_ids is not None:
            result["localIds"] = from_union([lambda x: from_dict(from_str, x), from_none], self.local_ids)
        if self.tax_ids is not None:
            result["taxIds"] = from_union([lambda x: from_list(lambda x: to_class(TaxIdentifier, x), x), from_none], self.tax_ids)
        if self.wallet is not None:
            result["wallet"] = from_union([from_str, from_none], self.wallet)
        return result


def person_from_dict(s: Any) -> Person:
    return Person.from_dict(s)


def person_to_dict(x: Person) -> Any:
    return to_class(Person, x)