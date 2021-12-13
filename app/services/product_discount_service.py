from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountSchema):

        try:
            if self.payment_method_repository.get_by_id(discount.payment_method_id).enabled :
                self.product_discount_repository.create(**discount.dict())
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Order creation Failed')