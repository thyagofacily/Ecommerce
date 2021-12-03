from pydantic import BaseModel
from enum import Enum


class DiscountMode(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'


class ProductDiscountSchema(BaseModel):
    product_id: int
    value: float
    payment_method_id: int
    mode: DiscountMode
