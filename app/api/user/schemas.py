from pydantic import BaseModel

from enum import Enum


class Role(str, Enum):
    ADMIN = 'admin'
    CUSTOMER = 'customer'


class UserSchema(BaseModel):
    display_name: str
    email: str
    password: str
    role: Role

class ShowUserSchema(BaseModel):
    display_name: str
    email: str
    role: Role

    class Config:
        orm_mode = True