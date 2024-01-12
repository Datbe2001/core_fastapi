from enum import Enum

from datetime import date
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreateParams(BaseModel):
    email: str
    username: str


class UserUpdateParams(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(BaseModel):
    id: str
    email: str
    username: str


class UserUpdate(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None


class LoginUser(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    id: str
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class UserResponse(UserBase):
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: int(v.timestamp())
        }
