class Room(object):
    def __init__(self):
        self._id = ""
        self._players = 0
        self._address = ""

    @property
    def players(self):
        return self._players

    @property
    def address(self):
        return self._address

    @property
    def id(self):
        return self._address
