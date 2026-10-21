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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ProcessingStatus(Enum):
    """Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
    the same one the asset carries.
    
    Where a pipeline stands on the thing it was given. Which move from which is a rule held
    beside the type, never in it.
    """
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"


@dataclass
class Job:
    """A piece of work the pipeline does to one asset: ingest it, read it, index it. The job is
    the record of the attempt — when it started, when it stopped, and what went wrong — never
    the work's output, which belongs to the asset it was done to.
    """
    asset: str
    """The asset being worked on, as the system that owns the asset names it. A job without one
    is not a job: there is nothing to process.
    """
    status: ProcessingStatus
    """Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
    the same one the asset carries.
    """
    created_at: Optional[datetime] = None
    """When the job was queued."""

    error_message: Optional[str] = None
    """What went wrong, as the worker reported it. Read by a person deciding whether to retry;
    never parsed.
    """
    finished_at: Optional[datetime] = None
    """When it stopped, whether it succeeded or failed. Absent while it runs."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    started_at: Optional[datetime] = None
    """When a worker picked it up, which is not when it was queued. Absent while it waits."""

    @staticmethod
    def from_dict(obj: Any) -> 'Job':
        assert isinstance(obj, dict)
        asset = from_str(obj.get("asset"))
        status = ProcessingStatus(obj.get("status"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        error_message = from_union([from_str, from_none], obj.get("errorMessage"))
        finished_at = from_union([from_datetime, from_none], obj.get("finishedAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        started_at = from_union([from_datetime, from_none], obj.get("startedAt"))
        return Job(asset, status, created_at, error_message, finished_at, id, started_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        result["status"] = to_enum(ProcessingStatus, self.status)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.error_message is not None:
            result["errorMessage"] = from_union([from_str, from_none], self.error_message)
        if self.finished_at is not None:
            result["finishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.finished_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.started_at is not None:
            result["startedAt"] = from_union([lambda x: x.isoformat(), from_none], self.started_at)
        return result


def job_from_dict(s: Any) -> Job:
    return Job.from_dict(s)


def job_to_dict(x: Job) -> Any:
    return to_class(Job, x)