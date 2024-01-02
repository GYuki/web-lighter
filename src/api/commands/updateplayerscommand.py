from dependency_injector.wiring import Provide
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
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
    def __init__(self):
        super().__init__()

    async def handle(self, req: UpdatePlayersCountCommandRequest, room_repository: RoomRepository = Provide[Container.room_repository]):
        room = await room_repository.get_room(req.room_id)
        status = False
        if room is not None:
            room.players = req.players_count
            if room.players == room.max_players:  # prevent rooms from overflow
                await room_repository.delete_room(room.id)
            else:
                await room_repository.update_room(room)

        return UpdatePlayersCountCommandResponse(
            status
        )
