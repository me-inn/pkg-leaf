# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Format(Enum):
    CAPTIONS = "captions"
    CAROUSEL_COPY = "carousel_copy"
    CTA_VARIANTS = "cta_variants"
    HASHTAGS = "hashtags"
    HOOKS = "hooks"
    SHORT_SCRIPTS = "short_scripts"


@dataclass
class RepurposeRequested:
    """One piece of text somebody wants turned into several shorter ones. Unlike the other
    commands, the whole instruction travels in the event: the asking system holds no job of
    its own to read it back from. Keys are snake_case, not the camelCase the rest of leaf
    uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
    event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
    vectors. The shape follows the wire.
    """
    job_id: str
    """The job to report the work against, created by the pipeline if it does not exist yet."""

    session_id: str
    """The working session the request belongs to, which is where the brand voice and the
    defaults come from.
    """
    channel: Optional[str] = None
    """Where the result is headed, which changes how it is written. Free text: the channels
    belong to whoever publishes.
    """
    context: Optional[str] = None
    """The text to work from, in full. Not a reference to an asset: a repurpose can be asked of
    words that were never put in.
    """
    formats: Optional[List[Format]] = None
    """Which shapes to write. Anything outside the list is dropped rather than refused, and a
    request left with none is not worked.
    """
    instructions: Optional[str] = None
    """Anything else the asker wants said, in their own words."""

    language: Optional[str] = None
    """BCP-47 tag of the language to write in. Detected from the context when absent."""

    objective: Optional[str] = None
    """What the result is for, in the vocabulary of whoever asked."""

    use_brand_voice: Optional[bool] = None
    """Whether to write in the brand voice held for the session. False writes neutrally."""

    @staticmethod
    def from_dict(obj: Any) -> 'RepurposeRequested':
        assert isinstance(obj, dict)
        job_id = from_str(obj.get("job_id"))
        session_id = from_str(obj.get("session_id"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        context = from_union([from_str, from_none], obj.get("context"))
        formats = from_union([lambda x: from_list(Format, x), from_none], obj.get("formats"))
        instructions = from_union([from_str, from_none], obj.get("instructions"))
        language = from_union([from_str, from_none], obj.get("language"))
        objective = from_union([from_str, from_none], obj.get("objective"))
        use_brand_voice = from_union([from_bool, from_none], obj.get("use_brand_voice"))
        return RepurposeRequested(job_id, session_id, channel, context, formats, instructions, language, objective, use_brand_voice)

    def to_dict(self) -> dict:
        result: dict = {}
        result["job_id"] = from_str(self.job_id)
        result["session_id"] = from_str(self.session_id)
        if self.channel is not None:
            result["channel"] = from_union([from_str, from_none], self.channel)
        if self.context is not None:
            result["context"] = from_union([from_str, from_none], self.context)
        if self.formats is not None:
            result["formats"] = from_union([lambda x: from_list(lambda x: to_enum(Format, x), x), from_none], self.formats)
        if self.instructions is not None:
            result["instructions"] = from_union([from_str, from_none], self.instructions)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.objective is not None:
            result["objective"] = from_union([from_str, from_none], self.objective)
        if self.use_brand_voice is not None:
            result["use_brand_voice"] = from_union([from_bool, from_none], self.use_brand_voice)
        return result


def repurpose_requested_from_dict(s: Any) -> RepurposeRequested:
    return RepurposeRequested.from_dict(s)


def repurpose_requested_to_dict(x: RepurposeRequested) -> Any:
    return to_class(RepurposeRequested, x)