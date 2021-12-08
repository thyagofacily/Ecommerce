from typing import List, Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    quantity: int


class OrderSchema(BaseModel):
    address_id: int
    payment_method_id: int
    coupon_code: Optional[str] = None
    products: List[ProductSchema]
