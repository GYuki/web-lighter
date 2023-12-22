class ServerLoad(object):
    def __init__(self, value=0):
        self._value = value

    def set_load(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
