from fastapi import APIRouter

from app.api.endpoint import (user)

route = APIRouter()

route.include_router(user.router, tags=["users"])