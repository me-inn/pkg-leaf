# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast
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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Severity(Enum):
    """How bad it is, as judged where it was raised."""

    CRITICAL = "critical"
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"


class Status(Enum):
    """Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
    by whoever raised it.
    """
    ACKNOWLEDGED = "acknowledged"
    REPORTED = "reported"
    RESOLVED = "resolved"


@dataclass
class SignalError:
    """Something in the pipeline broke, said in a way another system can route rather than only
    print. The only event not about one piece of content: it is about a step that failed and
    who answers for it. Keys are snake_case, not the camelCase the rest of leaf uses: this
    travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
    owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
    follows the wire.
    """
    code: str
    """A machine-readable code such as ENRICHMENT_TIMEOUT. Free text: the vocabulary belongs to
    whoever raised it, and a reader matches on it rather than on the summary.
    """
    occurred_at: datetime
    """When the failure happened. Carried inside the payload as well as on the event, because
    the signal outlives the event that delivered it.
    """
    owner_unit_ref: str
    """The session or unit the failure belongs to. Who answers for it, which is how an error
    finds somebody at all.
    """
    severity: Severity
    """How bad it is, as judged where it was raised."""

    signal_id: str
    """The signal's own id, written where it was raised, so the same failure reported twice can
    be recognised as one.
    """
    source: str
    """The module that raised it, such as creativeflow.worker.process_asset. Says where to look,
    not who is at fault.
    """
    status: Status
    """Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
    by whoever raised it.
    """
    summary: str
    """What went wrong, for a person. Never the whole trace."""

    correlation_id: Optional[str] = None
    """The trace this failure belongs to, for tying it to others from the same run."""

    metadata: Optional[Dict[str, Any]] = None
    """Whatever else the raising step knew — the asset, the stage it stopped at. Keys belong to
    that step, so none are fixed here.
    """
    subject_ref: Optional[str] = None
    """The thing that was being worked on when it broke, when there is one."""

    @staticmethod
    def from_dict(obj: Any) -> 'SignalError':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        occurred_at = from_datetime(obj.get("occurred_at"))
        owner_unit_ref = from_str(obj.get("owner_unit_ref"))
        severity = Severity(obj.get("severity"))
        signal_id = from_str(obj.get("signal_id"))
        source = from_str(obj.get("source"))
        status = Status(obj.get("status"))
        summary = from_str(obj.get("summary"))
        correlation_id = from_union([from_str, from_none], obj.get("correlation_id"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        subject_ref = from_union([from_str, from_none], obj.get("subject_ref"))
        return SignalError(code, occurred_at, owner_unit_ref, severity, signal_id, source, status, summary, correlation_id, metadata, subject_ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["occurred_at"] = self.occurred_at.isoformat()
        result["owner_unit_ref"] = from_str(self.owner_unit_ref)
        result["severity"] = to_enum(Severity, self.severity)
        result["signal_id"] = from_str(self.signal_id)
        result["source"] = from_str(self.source)
        result["status"] = to_enum(Status, self.status)
        result["summary"] = from_str(self.summary)
        if self.correlation_id is not None:
            result["correlation_id"] = from_union([from_str, from_none], self.correlation_id)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        if self.subject_ref is not None:
            result["subject_ref"] = from_union([from_str, from_none], self.subject_ref)
        return result


def signal_error_from_dict(s: Any) -> SignalError:
    return SignalError.from_dict(s)


def signal_error_to_dict(x: SignalError) -> Any:
    return to_class(SignalError, x)