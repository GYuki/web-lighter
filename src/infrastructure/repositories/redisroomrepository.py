from redis.asyncio import Redis

from src.domain.models.room.roomrepository import RoomRepository
from src.infrastructure.mappers.redis.room import RedisRoomMapper


class RedisRoomRepository(RoomRepository):
    def __init__(self, connection: Redis):
        self._connection = connection

    async def create_room(self, room):
        result = await self.update_room(room)
        return result

    async def get_room(self, room_id):
        room = await self._connection.hget("rooms", room_id)
        return RedisRoomMapper.map_from_redis(room)

    async def get_random_room(self):
        room = await self._connection.hrandfield("rooms", 1, withvalues=True)
        return RedisRoomMapper.map_to_redis(room)

    async def delete_room(self, room_id):
        await self._connection.hdel("rooms", room_id)
        return True

    async def update_room(self, room):
        await self._connection.hset("rooms", room.id, RedisRoomMapper.map_to_redis(room))
        return True

