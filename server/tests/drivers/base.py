from abc import ABC, abstractmethod


class Driver(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def app_is_running(self):
        pass
