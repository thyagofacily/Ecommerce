from fastapi import APIRouter
from fastapi.param_functions import Depends

from app.services.product_discount_service import ProductDiscountService
from .schemas import ProductDiscountSchema

router = APIRouter()


@router.post('/')
def create(discount: ProductDiscountSchema, service: ProductDiscountService = Depends()):
    service.create_discount(discount)
