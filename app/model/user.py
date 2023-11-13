from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship

from app.model.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(String(255), primary_key=True)
    username = Column(String(42), nullable=False)
    full_name = Column(String(42), nullable=True)
    phone = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False)

