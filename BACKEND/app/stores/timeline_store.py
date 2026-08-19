from threading import RLock
from typing import Optional

from app.models.frame import FrameContext


class TimelineStore:

    def __init__(self):

        self._frames: dict[
            str,
            dict[int, FrameContext]
        ] = {}

        self._lock = RLock()


    def create_session(
        self,
        session_id: str
    ):

        with self._lock:

            self._frames.setdefault(
                session_id,
                {}
            )


    def put(
        self,
        frame: FrameContext
    ):

        with self._lock:

            self._frames.setdefault(
                frame.session_id,
                {}
            )

            self._frames[
                frame.session_id
            ][
                frame.frame_id
            ] = frame


    def get(
        self,
        session_id: str,
        frame_id: int
    ) -> Optional[FrameContext]:

        with self._lock:

            return (

                self._frames
                .get(session_id, {})
                .get(frame_id)

            )


    def get_range(
        self,
        session_id: str,
        start_frame: int,
        end_frame: int
    ):

        with self._lock:

            frames = (
                self._frames
                .get(session_id, {})
            )

            return [

                frames[frame_id]

                for frame_id in range(
                    start_frame,
                    end_frame + 1
                )

                if frame_id in frames
            ]


    def count(
        self,
        session_id: str
    ) -> int:

        with self._lock:

            return len(
                self._frames.get(
                    session_id,
                    {}
                )
            )


    def clear(
        self,
        session_id: str
    ):

        with self._lock:

            self._frames.pop(
                session_id,
                None
            )