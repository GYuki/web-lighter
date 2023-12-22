from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.domain.models.room.room import Room
from src.domain.models.room.roomrepository import RoomRepository


class CreateRoomCommandRequest(BaseRequest):
    def __init__(self, max_players, address):
        super().__init__()
        self._address = address
        self._max_players = max_players

    @property
    def address(self):
        return self._address

    @property
    def max_players(self):
        return self._max_players


class CreateRoomCommandResponse(BaseResponse):
    def __init__(self, status, room):
        super().__init__()
        self._status = status
        self._room = room

    @property
    def status(self):
        return self._status

    @property
    def room(self):
        return self._room


class CreateCommandHandler(BaseHandler):
    def __init__(self, repository: RoomRepository):
        super().__init__()
        self._repository = repository

    async def handle(self, req: CreateRoomCommandRequest):
        room = Room(
            address=req.address,
            max_players=req.max_players
        )

        status = await self._repository.create_room(room)
        return CreateRoomCommandResponse(
            status,
            room
        )
