# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Any, Optional, TypeVar, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


@dataclass
class CropParams:
    """The rectangle to keep, in pixels from the top left of the original."""

    height: int
    """How tall the kept rectangle is, in pixels."""

    width: int
    """How wide the kept rectangle is, in pixels."""

    x: int
    """Pixels from the left edge of the original to the left edge of the rectangle."""

    y: int
    """Pixels from the top edge of the original to the top edge of the rectangle."""

    @staticmethod
    def from_dict(obj: Any) -> 'CropParams':
        assert isinstance(obj, dict)
        height = from_int(obj.get("height"))
        width = from_int(obj.get("width"))
        x = from_int(obj.get("x"))
        y = from_int(obj.get("y"))
        return CropParams(height, width, x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["height"] = from_int(self.height)
        result["width"] = from_int(self.width)
        result["x"] = from_int(self.x)
        result["y"] = from_int(self.y)
        return result


@dataclass
class FilterParams:
    """How to treat the image. The four multipliers leave it alone at 1."""

    blur: Optional[float] = None
    """Gaussian sigma. 0 is no blur."""

    brightness: Optional[float] = None
    """Multiplier on how light it is. Below 1 darkens, above 1 lightens."""

    contrast: Optional[float] = None
    """Multiplier on the distance between light and dark. Below 1 flattens, above 1 deepens."""

    saturation: Optional[float] = None
    """0 is grey."""

    sharpness: Optional[float] = None
    """Multiplier on edge definition. Below 1 softens, above 1 sharpens."""

    vignette: Optional[bool] = None
    """Whether to darken the corners. On or off: how much is the editor's to decide."""

    @staticmethod
    def from_dict(obj: Any) -> 'FilterParams':
        assert isinstance(obj, dict)
        blur = from_union([from_float, from_none], obj.get("blur"))
        brightness = from_union([from_float, from_none], obj.get("brightness"))
        contrast = from_union([from_float, from_none], obj.get("contrast"))
        saturation = from_union([from_float, from_none], obj.get("saturation"))
        sharpness = from_union([from_float, from_none], obj.get("sharpness"))
        vignette = from_union([from_bool, from_none], obj.get("vignette"))
        return FilterParams(blur, brightness, contrast, saturation, sharpness, vignette)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.blur is not None:
            result["blur"] = from_union([to_float, from_none], self.blur)
        if self.brightness is not None:
            result["brightness"] = from_union([to_float, from_none], self.brightness)
        if self.contrast is not None:
            result["contrast"] = from_union([to_float, from_none], self.contrast)
        if self.saturation is not None:
            result["saturation"] = from_union([to_float, from_none], self.saturation)
        if self.sharpness is not None:
            result["sharpness"] = from_union([to_float, from_none], self.sharpness)
        if self.vignette is not None:
            result["vignette"] = from_union([from_bool, from_none], self.vignette)
        return result


class Preset(Enum):
    """A named size belonging to a channel. What each one resolves to is the editor's to know,
    not this shape's.
    """
    IG_FEED = "ig_feed"
    IG_LANDSCAPE = "ig_landscape"
    IG_REELS = "ig_reels"
    IG_STORY = "ig_story"
    TIKTOK = "tiktok"


@dataclass
class ResizeParams:
    """The size to come out at, said either by naming a channel's preset or by giving both sides."""

    height: Optional[int] = None
    """How tall to come out, in pixels. Given together with width, instead of a preset."""

    preset: Optional[Preset] = None
    """A named size belonging to a channel. What each one resolves to is the editor's to know,
    not this shape's.
    """
    width: Optional[int] = None
    """How wide to come out, in pixels. Given together with height, instead of a preset."""

    @staticmethod
    def from_dict(obj: Any) -> 'ResizeParams':
        assert isinstance(obj, dict)
        height = from_union([from_int, from_none], obj.get("height"))
        preset = from_union([Preset, from_none], obj.get("preset"))
        width = from_union([from_int, from_none], obj.get("width"))
        return ResizeParams(height, preset, width)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.preset is not None:
            result["preset"] = from_union([lambda x: to_enum(Preset, x), from_none], self.preset)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        return result


@dataclass
class TrimParams:
    """The stretch to keep, in seconds from the start. Video only."""

    end_seconds: float
    """Where the kept stretch ends, in seconds from the start of the original."""

    start_seconds: float
    """Where the kept stretch begins, in seconds from the start of the original."""

    @staticmethod
    def from_dict(obj: Any) -> 'TrimParams':
        assert isinstance(obj, dict)
        end_seconds = from_float(obj.get("end_seconds"))
        start_seconds = from_float(obj.get("start_seconds"))
        return TrimParams(end_seconds, start_seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["end_seconds"] = to_float(self.end_seconds)
        result["start_seconds"] = to_float(self.start_seconds)
        return result


@dataclass
class EditParams:
    """What to do to it. Every step is optional and they apply together; an empty one copies the
    asset.
    """
    crop: Optional[CropParams] = None
    """The rectangle to keep, in pixels from the top left of the original."""

    filters: Optional[FilterParams] = None
    """How to treat the image. The four multipliers leave it alone at 1."""

    resize: Optional[ResizeParams] = None
    """The size to come out at, said either by naming a channel's preset or by giving both sides."""

    trim: Optional[TrimParams] = None
    """The stretch to keep, in seconds from the start. Video only."""

    @staticmethod
    def from_dict(obj: Any) -> 'EditParams':
        assert isinstance(obj, dict)
        crop = from_union([CropParams.from_dict, from_none], obj.get("crop"))
        filters = from_union([FilterParams.from_dict, from_none], obj.get("filters"))
        resize = from_union([ResizeParams.from_dict, from_none], obj.get("resize"))
        trim = from_union([TrimParams.from_dict, from_none], obj.get("trim"))
        return EditParams(crop, filters, resize, trim)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.crop is not None:
            result["crop"] = from_union([lambda x: to_class(CropParams, x), from_none], self.crop)
        if self.filters is not None:
            result["filters"] = from_union([lambda x: to_class(FilterParams, x), from_none], self.filters)
        if self.resize is not None:
            result["resize"] = from_union([lambda x: to_class(ResizeParams, x), from_none], self.resize)
        if self.trim is not None:
            result["trim"] = from_union([lambda x: to_class(TrimParams, x), from_none], self.trim)
        return result


@dataclass
class AssetEditRequested:
    """A cut, a resize or a filter somebody wants applied. The original is never changed: the
    result is a new asset. Keys are snake_case, not the camelCase the rest of leaf uses: this
    travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
    owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
    follows the wire.
    """
    asset_id: str
    """The asset to edit, which stays as it is."""

    job_id: str
    """The job to report the edit against."""

    edit_params: Optional[EditParams] = None
    """What to do to it. Every step is optional and they apply together; an empty one copies the
    asset.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'AssetEditRequested':
        assert isinstance(obj, dict)
        asset_id = from_str(obj.get("asset_id"))
        job_id = from_str(obj.get("job_id"))
        edit_params = from_union([EditParams.from_dict, from_none], obj.get("edit_params"))
        return AssetEditRequested(asset_id, job_id, edit_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset_id"] = from_str(self.asset_id)
        result["job_id"] = from_str(self.job_id)
        if self.edit_params is not None:
            result["edit_params"] = from_union([lambda x: to_class(EditParams, x), from_none], self.edit_params)
        return result


def asset_edit_requested_from_dict(s: Any) -> AssetEditRequested:
    return AssetEditRequested.from_dict(s)


def asset_edit_requested_to_dict(x: AssetEditRequested) -> Any:
    return to_class(AssetEditRequested, x)