from app.models import (
    FrameContext,
    VehicleDetection,
    PlateDetection,
    OCRResult,
    RecognitionResult
)


def test_frame_context():

    frame = FrameContext(

        session_id="session-1",

        frame_id=100,

        timestamp=3.333,

        width=1920,

        height=1080
    )

    assert frame.frame_id == 100

    assert frame.timestamp == 3.333

    assert frame.vehicles == []


def test_vehicle_detection():

    vehicle = VehicleDetection(

        session_id="session-1",

        frame_id=100,

        timestamp=3.333,

        vehicle_id=5,

        class_id=2,

        class_name="car",

        confidence=0.91,

        x1=100,

        y1=200,

        x2=500,

        y2=600
    )

    assert vehicle.vehicle_id == 5

    assert vehicle.class_name == "car"


def test_plate_detection():

    plate = PlateDetection(

        session_id="session-1",

        frame_id=100,

        timestamp=3.333,

        plate_id=1,

        x1=200,

        y1=400,

        x2=400,

        y2=450,

        confidence=0.89,

        vehicle_id=5
    )

    assert plate.plate_id == 1

    assert plate.vehicle_id == 5


def test_ocr_result():

    result = OCRResult(

        session_id="session-1",

        frame_id=100,

        timestamp=3.333,

        plate_id=1,

        vehicle_id=5,

        raw_text="KA02MH7256",

        confidence=0.87,

        preprocessing_variant="clahe",

        worker_id="ocr-1",

        latency_ms=25
    )

    assert result.raw_text == "KA02MH7256"


def test_recognition_result():

    result = RecognitionResult(

        session_id="session-1",

        plate_id=1,

        vehicle_id=5,

        raw_text="KA02MH7256",

        corrected_text="KA02MH7256",

        stable_plate="KA02MH7256",

        confidence=0.90,

        is_valid_format=True
    )

    assert result.resolved is False