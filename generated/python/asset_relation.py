# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AssetRelation:
    """One asset pointing at another, and what the pointing means. An edge rather than a column:
    an asset has no single related asset, and each kind of tie — one derived from another,
    one resembling another — would otherwise add a field to a thing it was never an attribute
    of.
    """
    from_asset: str
    """The id of the asset the tie starts at, in the system that owns it. The direction carries
    the meaning: derived_from read the other way is false.
    """
    relation_type: str
    """What the tie means, in the words of whoever drew it. Free text: the vocabulary belongs to
    the system that relates them.
    """
    to_asset: str
    """The id of the asset the tie points at, in the system that owns it."""

    created_at: Optional[datetime] = None
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'AssetRelation':
        assert isinstance(obj, dict)
        from_asset = from_str(obj.get("fromAsset"))
        relation_type = from_str(obj.get("relationType"))
        to_asset = from_str(obj.get("toAsset"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        return AssetRelation(from_asset, relation_type, to_asset, created_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fromAsset"] = from_str(self.from_asset)
        result["relationType"] = from_str(self.relation_type)
        result["toAsset"] = from_str(self.to_asset)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


def asset_relation_from_dict(s: Any) -> AssetRelation:
    return AssetRelation.from_dict(s)


def asset_relation_to_dict(x: AssetRelation) -> Any:
    return to_class(AssetRelation, x)