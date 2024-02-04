from pydantic import BaseModel


class CreateRoomRequest(BaseModel):
    room_id: str | None = ""
    max_players: int | None = None

