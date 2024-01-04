from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.api.queries.serverqueries import ServerQueries
from src.api.responses.server import Server
from src.container import Container

router = APIRouter(prefix='/servers')


@router.get("/best")
@inject
async def get_best_server(queries: ServerQueries = Depends(Provide[Container.server_queries])) -> Server:
    server = await queries.get_best_server()
    if server is None:
        raise HTTPException(status_code=404, detail="no server was found")

    return Server(
        address=server.address,
        ws_address=server.ws_address
    )
