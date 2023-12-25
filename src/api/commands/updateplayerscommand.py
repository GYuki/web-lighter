from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.domain.models.room.roomrepository import RoomRepository


class UpdatePlayersCountCommandRequest(BaseRequest):
    def __init__(self, players_count, room_id):
        super().__init__()
        self._players_count = players_count
        self._room_id = room_id

    @property
    def players_count(self):
        return self._players_count

    @property
    def room_id(self):
        return self._room_id


class UpdatePlayersCountCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class UpdatePlayersCountCommandHandler(BaseHandler):
    def __init__(self, repository: RoomRepository):
        super().__init__()
        self._repository = repository

    async def handle(self, req: UpdatePlayersCountCommandRequest):
        room = await self._repository.get_room(req.room_id)
        status = False
        if room is not None:
            room.players = req.players_count
            if room.players == room.max_players:  # prevent rooms from overflow
                await self._repository.delete_room(room.id)
            else:
                await self._repository.update_room(room)

        return UpdatePlayersCountCommandResponse(
            status
        )
