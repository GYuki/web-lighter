from pydantic import BaseModel


class Server(BaseModel):
    address: str
    ws_address: str
