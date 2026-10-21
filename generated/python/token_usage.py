# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class TokenUsage:
    """What one call to a model cost: who made it, which model answered, how many tokens each
    way, and the money. Separate from the credit ledger — credits are what the customer is
    charged, tokens are what the call actually consumed, and the two move for different
    reasons.
    """
    call_type: str
    """What the call was for, in the words of the system that made it. Free text: the kinds of
    call belong to that system.
    """
    cost_usd: float
    """What the call cost in US dollars, worked out when it was written from the prices in force
    then. Recorded rather than recomputed: prices change, and what was spent does not.
    """
    input_tokens: int
    """Tokens sent."""

    model: str
    """The model name as the provider gives it, verbatim. Kept exactly because the price was
    read against this string.
    """
    output_tokens: int
    """Tokens returned."""

    provider: str
    """Who served the call. Free text: providers are added without the shape changing."""

    created_at: Optional[datetime] = None
    """When the call was recorded."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    job: Optional[str] = None
    """The id of the job that made the call, in the system that owns jobs."""

    person: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever the call was made for. Absent for a
    call nobody is signed in behind, such as a background pass.
    """
    session: Optional[str] = None
    """The work session the call belongs to, as the system that owns the session names it.
    Absent when it belongs to none.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'TokenUsage':
        assert isinstance(obj, dict)
        call_type = from_str(obj.get("callType"))
        cost_usd = from_float(obj.get("costUsd"))
        input_tokens = from_int(obj.get("inputTokens"))
        model = from_str(obj.get("model"))
        output_tokens = from_int(obj.get("outputTokens"))
        provider = from_str(obj.get("provider"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        job = from_union([from_str, from_none], obj.get("job"))
        person = from_union([from_str, from_none], obj.get("person"))
        session = from_union([from_str, from_none], obj.get("session"))
        return TokenUsage(call_type, cost_usd, input_tokens, model, output_tokens, provider, created_at, id, job, person, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["callType"] = from_str(self.call_type)
        result["costUsd"] = to_float(self.cost_usd)
        result["inputTokens"] = from_int(self.input_tokens)
        result["model"] = from_str(self.model)
        result["outputTokens"] = from_int(self.output_tokens)
        result["provider"] = from_str(self.provider)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.job is not None:
            result["job"] = from_union([from_str, from_none], self.job)
        if self.person is not None:
            result["person"] = from_union([from_str, from_none], self.person)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def token_usage_from_dict(s: Any) -> TokenUsage:
    return TokenUsage.from_dict(s)


def token_usage_to_dict(x: TokenUsage) -> Any:
    return to_class(TokenUsage, x)