from fastapi.responses import JSONResponse
from fastapi import APIRouter


ping_router = APIRouter()


@ping_router.get("/ping/")
def ping_pong():
    return JSONResponse(
        status_code=200,
        content={"message": "pong"}
    )
