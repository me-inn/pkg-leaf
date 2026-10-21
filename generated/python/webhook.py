# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import List, Optional, Any, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Webhook:
    """A standing instruction to call a URL when something happens. The subscription only: what
    is to be called and for which events. No signing secret travels here — whoever signs a
    delivery holds the key for it, and a shared shape carrying it would be a secret in every
    system that read the shape.
    """
    events: List[str]
    """Which events to post. Free text: the names belong to whoever emits them, and a shape that
    fixed them would go stale the first time one is added.
    """
    url: str
    """Where to post. http or https, as given: a subscription to a URL that no longer answers is
    still a fact about what was asked for.
    """
    active: Optional[bool] = None
    """Whether it is still being called. Turned off rather than deleted, so the deliveries
    already made keep pointing at something.
    """
    created_at: Optional[datetime] = None
    """When the subscription was registered."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The session the subscription belongs to, as the system that owns the session names it.
    Deliveries are scoped by it, and so is who may read the subscription back. Optional:
    scoping a subscription to a working session is how Creative Flow holds it, not part of
    what it is, and a system without sessions must be able to carry the same shape.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'Webhook':
        assert isinstance(obj, dict)
        events = from_list(from_str, obj.get("events"))
        url = from_str(obj.get("url"))
        active = from_union([from_bool, from_none], obj.get("active"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        return Webhook(events, url, active, created_at, id, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["events"] = from_list(from_str, self.events)
        result["url"] = from_str(self.url)
        if self.active is not None:
            result["active"] = from_union([from_bool, from_none], self.active)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def webhook_from_dict(s: Any) -> Webhook:
    return Webhook.from_dict(s)


def webhook_to_dict(x: Webhook) -> Any:
    return to_class(Webhook, x)