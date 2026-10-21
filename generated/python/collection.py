# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
import dateutil.parser


T = TypeVar("T")


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Asset:
    asset: str
    """The id of the asset, in the system that owns it."""

    added_at: Optional[datetime] = None
    """When it was put in, which is not when the asset was recorded."""

    id: Optional[str] = None
    """The edge's own id in the system that holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'Asset':
        assert isinstance(obj, dict)
        asset = from_str(obj.get("asset"))
        added_at = from_union([from_datetime, from_none], obj.get("addedAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Asset(asset, added_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        if self.added_at is not None:
            result["addedAt"] = from_union([lambda x: x.isoformat(), from_none], self.added_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class Collection:
    """A named gathering of assets, made by a person because they belong together for a reason
    no pipeline would find. It holds no assets: it holds the edges that say which ones are in
    it, and when each was put there.
    """
    name: str
    """What it is called, in the words of whoever gathered it."""

    assets: Optional[List[Asset]] = None
    """The assets in it, each as its own edge: being in a collection is not an attribute of an
    asset, and the moment it was added belongs to the putting-in, not to either side.
    """
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    """Why these belong together. Written by a person; never derived from what is inside."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The id of the working session it was made in, in the system that owns the session. Absent
    when it was not made through one.
    """
    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Collection':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        assets = from_union([lambda x: from_list(Asset.from_dict, x), from_none], obj.get("assets"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return Collection(name, assets, created_at, description, id, session, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        if self.assets is not None:
            result["assets"] = from_union([lambda x: from_list(lambda x: to_class(Asset, x), x), from_none], self.assets)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def collection_from_dict(s: Any) -> Collection:
    return Collection.from_dict(s)


def collection_to_dict(x: Collection) -> Any:
    return to_class(Collection, x)