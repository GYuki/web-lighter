from src.domain.models.room.room import Room
import json


class RoomMapper(object):
    @classmethod
    def map_to_redis(cls, room: Room):
        return json.dumps(
            {
                "id": room.id,
                "players": room.players,
                "address": room.address
            }
        )

    @classmethod
    def map_from_redis(cls, room_string):
        room = json.loads(room_string)
        return Room(
            room['id'],
            room['players'],
            room['address']
        )
