from threading import RLock
from typing import Optional

from app.models.session import SessionState


class SessionManager:

    def __init__(self):

        self._sessions: dict[
            str,
            SessionState
        ] = {}

        self._lock = RLock()


    def create(
        self,
        session: SessionState
    ):

        with self._lock:

            self._sessions[
                session.session_id
            ] = session


    def get(
        self,
        session_id: str
    ) -> Optional[SessionState]:

        with self._lock:

            return self._sessions.get(
                session_id
            )


    def update(
        self,
        session_id: str,
        **kwargs
    ):

        with self._lock:

            session = self._sessions.get(
                session_id
            )

            if session is None:

                return None

            for key, value in kwargs.items():

                if hasattr(
                    session,
                    key
                ):

                    setattr(
                        session,
                        key,
                        value
                    )

            return session


    def delete(
        self,
        session_id: str
    ):

        with self._lock:

            self._sessions.pop(
                session_id,
                None
            )


    def all(self):

        with self._lock:

            return list(
                self._sessions.values()
            )