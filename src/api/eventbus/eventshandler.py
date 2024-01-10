from pydiator_core.mediatr import pydiator

from src.api.commands.createroomcommand import CreateRoomCommandRequest
from src.api.commands.createservercommand import CreateServerCommandRequest
from src.api.commands.deleteroomcommand import DeleteRoomCommandRequest
from src.api.commands.removeservercommand import RemoveServerCommandRequest
from src.api.commands.updateplayerscommand import UpdatePlayersCountCommandRequest
from src.api.commands.updateservercpucommand import UpdateServerCpuCommandRequest


async def on_server_cpu_update(msg):
    address = msg['address']
    cpu = msg['cpu']

    result = await pydiator.send(
        UpdateServerCpuCommandRequest(
            address=address,
            cpu=cpu
        )
    )


async def on_room_create(msg):
    address = msg['address']
    max_players = msg['max_players']
    players = msg['players']

    result = await pydiator.send(
        CreateRoomCommandRequest(
            address=address,
            max_players=max_players,
            players=players
        )
    )


async def on_server_create(msg):
    address = msg['address']
    domain = msg['domain']

    result = await pydiator.send(
        CreateServerCommandRequest(
            address=address,
            domain=domain
        )
    )


async def on_room_delete(msg):
    room_id = msg['room_id']

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
    players_count = msg['players']
    room_id = msg['room_id']

    result = await pydiator.send(
        UpdatePlayersCountCommandRequest(
            room_id=room_id,
            players_count=players_count
        )
    )
