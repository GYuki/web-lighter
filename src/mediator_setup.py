from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer

from src.api.commands.createroomcommand import CreateRoomCommandRequest, CreateCommandHandler
from src.api.commands.createservercommand import CreateServerCommandRequest, CreateServerCommandHandler
from src.api.commands.deleteroomcommand import DeleteRoomCommandRequest, DeleteRoomCommandHandler
from src.api.commands.removeservercommand import RemoveServerCommandRequest, RemoveServerCommandHandler
from src.api.commands.updateplayerscommand import UpdatePlayersCountCommandRequest, UpdatePlayersCountCommandHandler
from src.api.commands.updateservercpucommand import UpdateServerCpuCommandRequest, UpdateServerCpuCommandHandler
from src.api.notifications.roomcreatednotification import RoomCreatedNotification, RoomCreatedNotificationHandler


def set_up():
    pydiator_container = MediatrContainer()
    pydiator_container.register_request(CreateRoomCommandRequest, CreateCommandHandler())
    pydiator_container.register_request(CreateServerCommandRequest, CreateServerCommandHandler())
    pydiator_container.register_request(DeleteRoomCommandRequest, DeleteRoomCommandHandler())
    pydiator_container.register_request(RemoveServerCommandRequest, RemoveServerCommandHandler())
    pydiator_container.register_request(UpdatePlayersCountCommandRequest, UpdatePlayersCountCommandHandler())
    pydiator_container.register_request(UpdateServerCpuCommandRequest, UpdateServerCpuCommandHandler())
    pydiator_container.register_notification(RoomCreatedNotification, [RoomCreatedNotificationHandler()])

    pydiator.ready(container=pydiator_container)
