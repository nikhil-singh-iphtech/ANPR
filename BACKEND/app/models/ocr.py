from dataclasses import dataclass
from typing import Optional


@dataclass
class OCRResult:

    session_id: str

    frame_id: int

    timestamp: float

    plate_id: int

    # Vehicle relationship if known

    vehicle_id: Optional[int]

    # -----------------------------
    # OCR output
    # -----------------------------

    raw_text: str

    confidence: float

    # -----------------------------
    # Processing information
    # -----------------------------

    preprocessing_variant: str

    worker_id: str

    latency_ms: float