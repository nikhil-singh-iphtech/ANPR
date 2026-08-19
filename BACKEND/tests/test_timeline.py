from app.models.frame import (
    create_frame_context
)

from app.stores.timeline_store import (
    TimelineStore
)


def test_timeline_store():

    store = TimelineStore()

    session_id = "session-1"

    store.create_session(
        session_id
    )

    frame = create_frame_context(

        session_id=session_id,

        frame_id=30,

        fps=30,

        width=1920,

        height=1080
    )

    store.put(frame)

    result = store.get(

        session_id,

        30
    )

    assert result is not None

    assert result.frame_id == 30

    assert abs(
        result.timestamp - 1.0
    ) < 0.001


def test_timeline_range():

    store = TimelineStore()

    session_id = "session-2"

    store.create_session(
        session_id
    )

    for frame_id in range(10):

        frame = create_frame_context(

            session_id=session_id,

            frame_id=frame_id,

            fps=30,

            width=1920,

            height=1080
        )

        store.put(frame)

    result = store.get_range(

        session_id,

        3,

        7
    )

    assert len(result) == 5

    assert result[0].frame_id == 3

    assert result[-1].frame_id == 7