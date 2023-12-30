from dependency_injector.wiring import inject, Provide
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
from src.domain.models.room.room import Room
from src.domain.models.room.roomrepository import RoomRepository


class CreateRoomCommandRequest(BaseRequest):
    def __init__(self, max_players, address, players=0):
        super().__init__()
        self._address = address
        self._max_players = max_players
        self._players = 0

    @property
    def address(self):
        return self._address

    @property
    def max_players(self):
        return self._max_players

    @property
    def players(self):
        return self._players


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
    def __init__(self):
        super().__init__()

    @inject
    async def handle(self, req: CreateRoomCommandRequest, room_repository: RoomRepository = Provide[Container.room_repository]):
        room = Room(
            address=req.address,
            max_players=req.max_players,
            players=req.players
        )

        status = await room_repository.create_room(room)
        return CreateRoomCommandResponse(
            status,
            room
        )
