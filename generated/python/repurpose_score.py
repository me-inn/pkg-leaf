# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Any, Optional, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
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


class Format(Enum):
    """Which of the job's outputs this score is for. One score per format, so the job's own id
    does not identify a record.
    """
    CAPTIONS = "captions"
    CAROUSEL_COPY = "carousel_copy"
    CTA_VARIANTS = "cta_variants"
    HASHTAGS = "hashtags"
    HOOKS = "hooks"
    SHORT_SCRIPTS = "short_scripts"


@dataclass
class CreativeReading:
    """What the scorer made of that one output. The same shape a creative score carries, read
    against the channel the format is meant for.
    
    What a model made of a piece of work: how it sat against the voice it was written for,
    how it fitted the channel it was written into, and why. About the work, never about
    whoever asked for it — nothing here is said about an actor, so none of it is testimony.
    """
    brand_voice_score: float
    """How close the work came to the voice it was written for, from 0 to 1. The range is what
    the scorer produces, and keeping a number inside it is the job of the code that writes
    the record.
    """
    channel_fit_score: float
    """How well the work fitted the channel it was written into, from 0 to 1, on the same scale."""

    overall_score: float
    """The single number carried alongside the two others, from 0 to 1. Stated rather than
    derived here: how the scorer weighed voice against fit is its own, and recomputing it
    elsewhere would invent a weighting nobody agreed to.
    """
    reasoning: str
    """Why those numbers, in the scorer's own words. Kept because a number with no account of
    itself cannot be argued with.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'CreativeReading':
        assert isinstance(obj, dict)
        brand_voice_score = from_float(obj.get("brandVoiceScore"))
        channel_fit_score = from_float(obj.get("channelFitScore"))
        overall_score = from_float(obj.get("overallScore"))
        reasoning = from_str(obj.get("reasoning"))
        return CreativeReading(brand_voice_score, channel_fit_score, overall_score, reasoning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["brandVoiceScore"] = to_float(self.brand_voice_score)
        result["channelFitScore"] = to_float(self.channel_fit_score)
        result["overallScore"] = to_float(self.overall_score)
        result["reasoning"] = from_str(self.reasoning)
        return result


@dataclass
class RepurposeScore:
    """The same reading as a creative score, but of work a job turned into one other format. It
    is its own record and not a column on the job: one job produces several formats, and each
    is read on its own.
    """
    format: Format
    """Which of the job's outputs this score is for. One score per format, so the job's own id
    does not identify a record.
    """
    job: str
    """The id of the repurpose job that produced the work, in the system that ran it."""

    reading: CreativeReading
    """What the scorer made of that one output. The same shape a creative score carries, read
    against the channel the format is meant for.
    """
    created_at: Optional[datetime] = None
    """When the output was scored, which is not when the job ran."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    @staticmethod
    def from_dict(obj: Any) -> 'RepurposeScore':
        assert isinstance(obj, dict)
        format = Format(obj.get("format"))
        job = from_str(obj.get("job"))
        reading = CreativeReading.from_dict(obj.get("reading"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        return RepurposeScore(format, job, reading, created_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = to_enum(Format, self.format)
        result["job"] = from_str(self.job)
        result["reading"] = to_class(CreativeReading, self.reading)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


def repurpose_score_from_dict(s: Any) -> RepurposeScore:
    return RepurposeScore.from_dict(s)


def repurpose_score_to_dict(x: RepurposeScore) -> Any:
    return to_class(RepurposeScore, x)