class Room(object):
    def __init__(self, _id="", _players=0, _address=""):
        self._id = _id
        self.players = _players
        self._address = _address

    @property
    def address(self):
        return self._address

    @property
    def id(self):
        return self._address
