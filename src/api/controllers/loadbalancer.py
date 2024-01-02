from dependency_injector.wiring import inject, Provide
from fastapi import HTTPException, APIRouter, Depends
from src.api.queries.roomqueries import RoomQueries
from src.api.responses.room import Room
from src.container import Container


router = APIRouter(prefix='/rooms')


@router.get("/{room_id}")
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
