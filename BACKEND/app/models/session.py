from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class JobStatus(str, Enum):

    CREATED = "CREATED"

    QUEUED = "QUEUED"

    PROCESSING = "PROCESSING"

    FINALIZING = "FINALIZING"

    READY_TO_PLAY = "READY_TO_PLAY"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"


@dataclass
class SessionState:

    session_id: str

    video_path: str

    original_filename: str

    status: JobStatus = JobStatus.CREATED

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    started_at: Optional[datetime] = None

    completed_at: Optional[datetime] = None

    error_message: Optional[str] = None

    # -----------------------------
    # Video metadata
    # -----------------------------

    fps: float = 0.0

    total_frames: int = 0

    width: int = 0

    height: int = 0

    duration: float = 0.0

    # -----------------------------
    # Processing progress
    # -----------------------------

    processed_frames: int = 0

    processed_timestamp: float = 0.0

    progress_percent: float = 0.0