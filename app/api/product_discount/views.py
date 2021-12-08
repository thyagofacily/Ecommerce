from fastapi import APIRouter
from fastapi.param_functions import Depends

from app.services.product_discount_service import ProductDiscountService
from .schemas import ProductDiscountSchema
from app.services.auth_service import get_user, only_admin


router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/')
def create(discount: ProductDiscountSchema, service: ProductDiscountService = Depends()):
    service.create_discount(discount)
