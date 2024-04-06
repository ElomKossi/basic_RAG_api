from fastapi import APIRouter 

from starlette import status
from starlette.requests import Request

# we define a router to hold all our core endpoints together
router = APIRouter(tags=["Core Endpoints"])  

@router.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck(request: Request) -> dict:
    return {"version": request.app.version}