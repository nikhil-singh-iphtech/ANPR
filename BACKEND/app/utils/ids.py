import uuid


def create_session_id() -> str:

    return str(
        uuid.uuid4()
    )


def create_plate_id() -> str:

    return str(
        uuid.uuid4()
    )