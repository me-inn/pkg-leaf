# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast
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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AIJob:
    """A short-lived record of an asynchronous model call — a generation, a retrieval answer, an
    edit, a repurpose. Separate from job: a job is work done to one asset and reports timing,
    this is work asked for inside a session and reports an answer. The two are kept apart
    rather than merged behind a discriminator because they do not agree on what is required
    or on what is kept.
    """
    job_type: str
    """Which kind of call was asked for. Free text: the vocabulary belongs to whoever queues the
    job, and it grows every time a new flow is added.
    """
    status: str
    """Where the call got to. Free text here, unlike job: the column carries no enum and each
    flow writes its own words.
    """
    created_at: Optional[datetime] = None
    """When the call was queued."""

    error_message: Optional[str] = None
    """What went wrong, as the worker reported it. Read by a person; never parsed."""

    id: Optional[str] = None
    """The record's own id in the system that holds it. It is what the caller polls with."""

    result: Optional[Dict[str, Any]] = None
    """What came back, in the shape the job type produces. Left open on purpose: a repurpose
    result and a retrieval answer have nothing in common, and declaring one shape for both
    would describe neither.
    """
    session: Optional[str] = None
    """The session the job was asked for, as the system that owns the session names it. It is
    what keeps one session from reading another's answer. Absent on rows written before jobs
    were scoped.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'AIJob':
        assert isinstance(obj, dict)
        job_type = from_str(obj.get("jobType"))
        status = from_str(obj.get("status"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        error_message = from_union([from_str, from_none], obj.get("errorMessage"))
        id = from_union([from_str, from_none], obj.get("id"))
        result = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("result"))
        session = from_union([from_str, from_none], obj.get("session"))
        return AIJob(job_type, status, created_at, error_message, id, result, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["jobType"] = from_str(self.job_type)
        result["status"] = from_str(self.status)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.error_message is not None:
            result["errorMessage"] = from_union([from_str, from_none], self.error_message)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.result is not None:
            result["result"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.result)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def ai_job_from_dict(s: Any) -> AIJob:
    return AIJob.from_dict(s)


def ai_job_to_dict(x: AIJob) -> Any:
    return to_class(AIJob, x)