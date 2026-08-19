from dataclasses import dataclass, field
from typing import Any


@dataclass
class FrameContext:

    # -----------------------------
    # Identity
    # -----------------------------

    session_id: str

    frame_id: int

    timestamp: float

    # -----------------------------
    # Video dimensions
    # -----------------------------

    width: int

    height: int

    # -----------------------------
    # Pipeline results
    # -----------------------------

    vehicles: list[dict[str, Any]] = field(
        default_factory=list
    )

    plates: list[dict[str, Any]] = field(
        default_factory=list
    )

    ocr_results: list[dict[str, Any]] = field(
        default_factory=list
    )

    recognition_events: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

def create_frame_context(
    session_id: str,
    frame_id: int,
    fps: float,
    width: int,
    height: int
) -> FrameContext:

    timestamp = (
        frame_id / fps
        if fps > 0
        else 0.0
    )

    return FrameContext(

        session_id=session_id,

        frame_id=frame_id,

        timestamp=timestamp,

        width=width,

        height=height
    )