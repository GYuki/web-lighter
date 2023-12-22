from src.domain.models.room.roomrepository import RoomRepository


class RoomQueries(object):
    def __init__(self, repository: RoomRepository):
        self._repository = repository

    def get_room_by_id(self, room_id):
        return self._repository.get_room(room_id)

    def get_random_room(self):
        return self._repository.get_random_room()
