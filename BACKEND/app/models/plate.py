from dataclasses import dataclass
from typing import Optional


@dataclass
class PlateDetection:

    session_id: str

    frame_id: int

    timestamp: float

    plate_id: int

    # -----------------------------
    # Plate location
    # -----------------------------

    x1: float

    y1: float

    x2: float

    y2: float

    confidence: float

    # -----------------------------
    # Relationship to vehicle
    # -----------------------------

    vehicle_id: Optional[int] = None

    # -----------------------------
    # Quality
    # -----------------------------

    quality_score: float = 0.0

    is_good_quality: bool = False