from dataclasses import dataclass
from typing import Optional


@dataclass
class RecognitionResult:

    session_id: str

    plate_id: int

    vehicle_id: Optional[int]

    # -----------------------------
    # Final recognition
    # -----------------------------

    raw_text: str

    corrected_text: str

    stable_plate: Optional[str]

    confidence: float

    # -----------------------------
    # Validation
    # -----------------------------

    is_valid_format: bool

    # -----------------------------
    # Database
    # -----------------------------

    database_match: bool = False

    owner_name: Optional[str] = None

    access_status: Optional[str] = None

    # -----------------------------
    # State
    # -----------------------------

    resolved: bool = False