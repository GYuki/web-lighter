from dependency_injector.wiring import inject, Provide
from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

from src.container import Container
from src.domain.models.room.roomrepository import RoomRepository


class RoomCreatedNotification(BaseNotification):
    def __init__(self, room_id, address):
        super().__init__()
        self._room_id = room_id
        self._address = address

    @property
    def room_id(self):
        return self._room_id

    @property
    def address(self):
        return self._address
    

class RoomCreatedNotificationHandler(BaseNotificationHandler):
    @inject
    async def handle(self, notification: RoomCreatedNotification, room_repository: RoomRepository = Provide[Container.room_repository]):
        room = await room_repository.get_room(notification.room_id)
        room.address = notification.address

        await room_repository.update_room(room)
