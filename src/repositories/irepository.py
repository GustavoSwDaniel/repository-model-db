import abc


class IRepository(metaclass=abc.ABCMeta):
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory