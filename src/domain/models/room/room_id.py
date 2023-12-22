from uuid import uuid4


class RoomId(object):
    def __init__(self, id=""):
        self._value = str(uuid4()) if not id else id

    @property
    def value(self):
        return self._value
