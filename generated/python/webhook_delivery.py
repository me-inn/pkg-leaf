# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class WebhookDelivery:
    """One attempt to call a webhook: what was sent, what came back, and how many tries it took.
    A record of its own rather than a column on the subscription, because one subscription
    has many deliveries and each outlives the state of the next. No signature travels here,
    for the same reason none travels on the subscription.
    """
    event: str
    """Which event triggered the call. Free text, matching one of the names on the subscription."""

    webhook: str
    """The subscription this attempt was made for, as the system that holds it names it."""

    attempts: Optional[int] = None
    """How many times this delivery has been tried."""

    created_at: Optional[datetime] = None
    """When the attempt was recorded, which is not when the event happened."""

    http_status: Optional[int] = None
    """The status code the endpoint answered with. Absent when the call never got an answer — a
    timeout and a 500 are different failures.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    payload: Optional[Dict[str, Any]] = None
    """The body that was posted. Open on purpose: its keys belong to whoever emits the event,
    and the delivery only records what went out.
    """
    response_body: Optional[str] = None
    """What the endpoint wrote back, kept as given. Read when a delivery has to be explained,
    never parsed.
    """
    status: Optional[str] = None
    """Where the attempt stands. Free text rather than an enum: the source has no declared set,
    only a default of pending.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'WebhookDelivery':
        assert isinstance(obj, dict)
        event = from_str(obj.get("event"))
        webhook = from_str(obj.get("webhook"))
        attempts = from_union([from_int, from_none], obj.get("attempts"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        http_status = from_union([from_int, from_none], obj.get("httpStatus"))
        id = from_union([from_str, from_none], obj.get("id"))
        payload = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("payload"))
        response_body = from_union([from_str, from_none], obj.get("responseBody"))
        status = from_union([from_str, from_none], obj.get("status"))
        return WebhookDelivery(event, webhook, attempts, created_at, http_status, id, payload, response_body, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event"] = from_str(self.event)
        result["webhook"] = from_str(self.webhook)
        if self.attempts is not None:
            result["attempts"] = from_union([from_int, from_none], self.attempts)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.http_status is not None:
            result["httpStatus"] = from_union([from_int, from_none], self.http_status)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.payload is not None:
            result["payload"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.payload)
        if self.response_body is not None:
            result["responseBody"] = from_union([from_str, from_none], self.response_body)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        return result


def webhook_delivery_from_dict(s: Any) -> WebhookDelivery:
    return WebhookDelivery.from_dict(s)


def webhook_delivery_to_dict(x: WebhookDelivery) -> Any:
    return to_class(WebhookDelivery, x)