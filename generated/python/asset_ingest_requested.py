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
class AssetIngestRequested:
    """Somebody put a file in somewhere else and wants it read. The bytes are already in the
    store; only the two ids travel. Keys are snake_case, not the camelCase the rest of leaf
    uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
    event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
    vectors. The shape follows the wire.
    """
    asset_id: str
    """The asset to read, in the system that holds it."""

    job_id: str
    """The job to report the reading against. Written by whoever asked, so the asker can follow
    the work without waiting for a reply.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'AssetIngestRequested':
        assert isinstance(obj, dict)
        asset_id = from_str(obj.get("asset_id"))
        job_id = from_str(obj.get("job_id"))
        return AssetIngestRequested(asset_id, job_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset_id"] = from_str(self.asset_id)
        result["job_id"] = from_str(self.job_id)
        return result


def asset_ingest_requested_from_dict(s: Any) -> AssetIngestRequested:
    return AssetIngestRequested.from_dict(s)


def asset_ingest_requested_to_dict(x: AssetIngestRequested) -> Any:
    return to_class(AssetIngestRequested, x)