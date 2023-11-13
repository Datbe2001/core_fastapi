import logging

from typing import Optional
from sqlalchemy.orm import Session
from .base import CRUDBase
from ..model import User
from app.utils import hash_lib

from app.utils.hash_lib import hash_verify_code
from app.schemas.user import UserCreate, UserUpdate
from ..model.base import ConfirmStatusUser, UserSystemRole

logger = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
        current_user = db.query(User).filter(User.id == user_id).first()
        return current_user


crud_user = CRUDUser(User)
