from fastapi import APIRouter, Depends

from app.services.auth_service import only_customer

from .schemas import OrderSchema

router = APIRouter(dependencies=[Depends(only_customer)])


@router.post('/')
def create(order: OrderSchema):
    return order