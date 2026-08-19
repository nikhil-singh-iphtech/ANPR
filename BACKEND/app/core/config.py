from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # ----------------------------------
    # Application
    # ----------------------------------

    app_name: str = "ANPR Backend"

    app_env: str = "development"

    debug: bool = True


    # ----------------------------------
    # Server
    # ----------------------------------

    host: str = "127.0.0.1"

    port: int = 8000


    # ----------------------------------
    # Directories
    # ----------------------------------

    upload_dir: str = "uploads"

    result_dir: str = "results"

    model_dir: str = "models"

    log_dir: str = "logs"


    # ----------------------------------
    # Models
    # ----------------------------------

    vehicle_model: str = "models/yolo11s.pt"

    plate_model: str = "models/license_plate.pt"


    # ----------------------------------
    # Detection
    # ----------------------------------

    vehicle_confidence: float = 0.30

    plate_confidence: float = 0.30


    # ----------------------------------
    # Vehicle classes
    # ----------------------------------

    vehicle_classes: str = "2,5,7"


    # ----------------------------------
    # Tracker
    # ----------------------------------

    tracker: str = "bytetrack.yaml"


    # ----------------------------------
    # OCR
    # ----------------------------------

    ocr_workers: int = 2

    ocr_queue_size: int = 128

    ocr_min_confidence: float = 0.30

    ocr_frame_interval: int = 5


    # ----------------------------------
    # Plate quality
    # ----------------------------------

    plate_min_width: int = 80

    plate_min_height: int = 25

    plate_min_quality: float = 0.65


    # ----------------------------------
    # Temporal voting
    # ----------------------------------

    temporal_window: int = 15

    temporal_min_votes: int = 3

    temporal_min_confidence: float = 0.40


    # ----------------------------------
    # Processing
    # ----------------------------------

    process_workers: int = 1


    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        extra="ignore"
    )


    @property
    def base_dir(self) -> Path:

        return BASE_DIR


    @property
    def upload_path(self) -> Path:

        return BASE_DIR / self.upload_dir


    @property
    def result_path(self) -> Path:

        return BASE_DIR / self.result_dir


    @property
    def model_path(self) -> Path:

        return BASE_DIR / self.model_dir


    @property
    def log_path(self) -> Path:

        return BASE_DIR / self.log_dir


    @property
    def vehicle_class_ids(self) -> List[int]:

        return [

            int(x.strip())

            for x in
            self.vehicle_classes.split(",")

            if x.strip()
        ]


settings = Settings()


# --------------------------------------
# Create required directories
# --------------------------------------

settings.upload_path.mkdir(
    parents=True,
    exist_ok=True
)

settings.result_path.mkdir(
    parents=True,
    exist_ok=True
)

settings.model_path.mkdir(
    parents=True,
    exist_ok=True
)

settings.log_path.mkdir(
    parents=True,
    exist_ok=True
)