from queue import Queue

from app.core.config import settings


class PipelineQueues:

    def __init__(self):

        # --------------------------------
        # Vehicle detection
        # --------------------------------

        self.vehicle_detection_queue = Queue(
            maxsize=settings.ocr_queue_size
        )

        # --------------------------------
        # Plate detection
        # --------------------------------

        self.plate_detection_queue = Queue(
            maxsize=settings.ocr_queue_size
        )

        # --------------------------------
        # OCR
        # --------------------------------

        self.ocr_queue = Queue(
            maxsize=settings.ocr_queue_size
        )

        # --------------------------------
        # Recognition
        # --------------------------------

        self.recognition_queue = Queue(
            maxsize=settings.ocr_queue_size
        )

        # --------------------------------
        # Final results
        # --------------------------------

        self.result_queue = Queue(
            maxsize=settings.ocr_queue_size
        )