import json

from pydiator_core.mediatr import pydiator

from src.api.commands.createroomcommand import CreateRoomCommandRequest
from src.api.commands.createservercommand import CreateServerCommandRequest
from src.api.commands.deleteroomcommand import DeleteRoomCommandRequest
from src.api.commands.removeservercommand import RemoveServerCommandRequest
from src.api.commands.updateplayerscommand import UpdatePlayersCountCommandRequest
from src.api.commands.updateservercpucommand import UpdateServerCpuCommandRequest
from src.api.notifications.roomcreatednotification import RoomCreatedNotification


async def on_server_cpu_update(msg):
    data = json.loads(msg)
    address = data['address']
    cpu = data['cpu']

    result = await pydiator.send(
        UpdateServerCpuCommandRequest(
            address=address,
            cpu=cpu
        )
    )


async def on_room_create(msg):
    data = json.loads(msg)
    address = data['address']
    room_id = data['room_id']

    await pydiator.publish(
        RoomCreatedNotification(
            address=address,
            room_id=room_id
        )
    )


async def on_server_create(msg):
    data = json.loads(msg)
    address = data['address']
    domain = data['domain']

    result = await pydiator.send(
        CreateServerCommandRequest(
            address=address,
            domain=domain
        )
    )


async def on_room_delete(msg):
    data = json.loads(msg)
    room_id = data['room_id']

    result = await pydiator.send(
        DeleteRoomCommandRequest(
            room_id=room_id
        )
    )


async def on_server_remove(msg):
    address = msg['address']

    result = await pydiator.send(
        RemoveServerCommandRequest(
            address=address
        )
    )


async def on_room_players_update(msg):
    data = json.loads(msg)
    players_count = data['players']
    room_id = data['room_id']

    result = await pydiator.send(
        UpdatePlayersCountCommandRequest(
            room_id=room_id,
            players_count=players_count
        )
    )
