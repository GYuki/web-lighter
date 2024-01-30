from dependency_injector.wiring import inject, Provide
from fastapi import HTTPException, APIRouter, Depends
from pydiator_core.mediatr import pydiator

from src.api.commands.createroomcommand import CreateRoomCommandRequest
from src.api.queries.roomqueries import RoomQueries
from src.api.requests.createroom import CreateRoomRequest
from src.api.responses.room import Room
from src.container import Container


router = APIRouter(prefix='/rooms')


@router.get("/")
@inject
async def join_room(room_id: str = None, queries: RoomQueries = Depends(Provide[Container.room_queries])) -> Room:
    if not room_id:
        raise HTTPException(status_code=500, detail="Room id is empty or null")

    room = await queries.get_room_by_id(room_id)

    if room is None:
        raise HTTPException(status_code=404, detail="No room with such room id")

    return Room(
        id=room.id,
        address=room.address
    )


@router.get("/random/")
@inject
async def join_random_room(queries: RoomQueries = Depends(Provide[Container.room_queries])) -> Room:
    room = await queries.get_random_room()
    if room is None:
        raise HTTPException(status_code=404, detail="No random room was found")

    return Room(
        id=room.id,
        address=room.address
    )


@router.post("/create")
@inject
async def create_room(request: CreateRoomRequest) -> Room:
    result = await pydiator.send(
        CreateRoomCommandRequest(
            room_id=request.room_id,
            max_players=request.max_players
        )
    )

    if not result.status:
        raise HTTPException(status_code=422, detail="Could not create room")

    return Room(
        id=result.room.id
    )
