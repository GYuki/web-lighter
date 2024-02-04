from src.domain.models.room.room_id import RoomId


class Room(object):
    def __init__(self, room_id="", players=0, max_players=1, address=""):
        self._room_id = RoomId(room_id)
        self.players = players
        self._max_players = max_players
        self._address = address

    @property
    def address(self):
        return self._address

    @property
    def id(self):
        return self._room_id.value
    
    @property
    def max_players(self):
        return self._max_players

    def set_address(self, address):
        self._address = address
