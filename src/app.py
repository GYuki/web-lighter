import asyncio

from dependency_injector.wiring import inject, Provide
from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer

from src.api.commands.createroomcommand import CreateRoomCommandRequest, CreateCommandHandler
from src.api.queries.roomqueries import RoomQueries
from src.container import Container
from src.domain.models.room.roomrepository import RoomRepository


def set_up():
    pydiator_container = MediatrContainer()
    pydiator_container.register_request(CreateRoomCommandRequest, CreateCommandHandler())

    pydiator.ready(container=pydiator_container)


async def sample():
    await pydiator.send(
        CreateRoomCommandRequest(
            max_players=2,
            address='',
            players=0,
        )
    )

    await sample2()


async def sample2():
    await pydiator.send(
        CreateRoomCommandRequest(
            max_players=2,
            address='',
            players=0,
        )
    )


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    set_up()

    asyncio.run(sample())

    a = input()
