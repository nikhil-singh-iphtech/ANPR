from dataclasses import dataclass
from typing import Optional


@dataclass
class VehicleDetection:

    session_id: str

    frame_id: int

    timestamp: float

    vehicle_id: int

    class_id: int

    class_name: str

    confidence: float

    x1: float

    y1: float

    x2: float

    y2: float

    # -----------------------------
    # Tracking state
    # -----------------------------

    confirmed: bool = False

    lost: bool = False