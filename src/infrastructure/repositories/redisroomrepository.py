from redis import Redis

from src.domain.models.room.roomrepository import RoomRepository
from src.infrastructure.mappers.room import RoomMapper


class RedisRoomRepository(RoomRepository):
    def __init__(self, connection: Redis):
        self._connection = connection

    def create_room(self, room):
        return self.update_room(room)

    def get_room(self, room_id):
        return self._connection.hget("rooms", room_id)

    def delete_room(self, room_id):
        self._connection.hdel("rooms", room_id)
        return True

    def update_room(self, room):
        self._connection.hset("rooms", room.id, RoomMapper.map_to_redis(room))
        return True

