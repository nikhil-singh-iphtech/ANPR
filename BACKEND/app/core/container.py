from app.services.session_manager import (
    SessionManager
)

from app.services.queues import (
    PipelineQueues
)

from app.stores.timeline_store import (
    TimelineStore
)


class ApplicationContainer:

    def __init__(self):

        self.sessions = SessionManager()

        self.queues = PipelineQueues()

        self.timeline = TimelineStore()


container = ApplicationContainer()