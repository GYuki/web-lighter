from src.domain.models.room.room import Room
import json


class RedisRoomMapper(object):
    @classmethod
    def map_to_redis(cls, room: Room):
        return json.dumps(
            {
                'id': room.id,
                'players': room.players,
                'max_players': room.max_players,
                'address': room.address
            }
        )

    @classmethod
    def map_from_redis(cls, room_string):
        room = json.loads(room_string)
        return Room(
            room_id=room['id'],
            players=room['players'],
            address=room['address'],
            max_players=room['max_players']
        )
