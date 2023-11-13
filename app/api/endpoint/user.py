import logging

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.depend import oauth2
from app.constant.app_status import AppStatus
from app.db.database import get_db
from app.model import User
from app.services.user import UserService
from app.utils.response import make_response_object
from ...model.base import UserSystemRole

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/user/list")
async def list_users(skip=0,
                     limit=10,
                     system_role: UserSystemRole = None,
                     email: str = None,
                     username: str = None,
                     user: User = Depends(oauth2.admin),
                     db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.list_users(system_role=system_role, email=email,
                                                  username=username, skip=skip,
                                                  limit=limit)
    return make_response_object(user_response)


@router.get("/user/{user_id}/get_user")
async def get_user_by_id(user_id: str,
                         user: User = Depends(oauth2.get_current_user),
                         db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_user_by_id(user_id=user_id)
    return make_response_object(user_response)


@router.get("/user/me")
async def read_me(user: User = Depends(oauth2.get_current_user),
                  db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_user_by_id(user_id=user.id)
    return make_response_object(user_response)

