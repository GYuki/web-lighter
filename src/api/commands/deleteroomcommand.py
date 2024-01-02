from dependency_injector.wiring import Provide, inject
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
from src.domain.models.room.roomrepository import RoomRepository


class DeleteRoomCommandRequest(BaseRequest):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class DeleteRoomCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class DeleteRoomCommandHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    @inject
    async def handle(self, req: DeleteRoomCommandRequest, room_repository: RoomRepository = Provide[Container.room_repository]):
        status = await room_repository.delete_room(req.room_id)
        return DeleteRoomCommandResponse(
            status=status
        )
