from fastapi import APIRouter

from .schemas import OrderSchema

router = APIRouter()


@router.post('/')
def create(order: OrderSchema):
    return order