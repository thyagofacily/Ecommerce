from sqlalchemy.sql.sqltypes import DateTime
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class CouponType(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'

class CouponSchema(BaseModel):
    code : str
    expire_at : datetime
    limit: int
    type: CouponType
    value: float

class EditCouponSchema(BaseModel):
    expire_at: datetime
    limit: int

class ShowCouponSchema(CouponSchema):
    id: int 

    class Config:
        orm_mode = True