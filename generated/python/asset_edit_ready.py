# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AssetEditReady:
    """An edit was applied and saved as a new asset. Both ids travel, because the point of the
    event is the pair: the original still stands and this one came from it. Keys are
    snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
    envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
    snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
    """
    content_id: str
    """The new asset the edit became. Named contentId and not assetId so every result event
    points at its subject under one name.
    """
    original_asset_id: str
    """The asset that was edited, unchanged."""

    session_id: str
    """The working session the edit was made in."""

    storage_key: str
    """Where the edited bytes sit in the store that holds them. Meaningful only to that store."""

    @staticmethod
    def from_dict(obj: Any) -> 'AssetEditReady':
        assert isinstance(obj, dict)
        content_id = from_str(obj.get("content_id"))
        original_asset_id = from_str(obj.get("original_asset_id"))
        session_id = from_str(obj.get("session_id"))
        storage_key = from_str(obj.get("storage_key"))
        return AssetEditReady(content_id, original_asset_id, session_id, storage_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content_id"] = from_str(self.content_id)
        result["original_asset_id"] = from_str(self.original_asset_id)
        result["session_id"] = from_str(self.session_id)
        result["storage_key"] = from_str(self.storage_key)
        return result


def asset_edit_ready_from_dict(s: Any) -> AssetEditReady:
    return AssetEditReady.from_dict(s)


def asset_edit_ready_to_dict(x: AssetEditReady) -> Any:
    return to_class(AssetEditReady, x)