from .base import Driver


class UIDriver(Driver):
    def __init__(self):
        pass

    def app_is_running(self):
        raise Exception("Not implemented")
