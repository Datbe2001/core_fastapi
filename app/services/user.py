import uuid
import smtplib
import logging

from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.core.exceptions import error_exception_handler
from app.core.settings import settings

from ..schemas import UserResponse
from ..crud.user import crud_user

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def get_user_by_id(self, user_id: str):
        current_user = crud_user.get_user_by_id(db=self.db, user_id=user_id)
        if not current_user:
            return "loi"
        return UserResponse.from_orm(current_user)


