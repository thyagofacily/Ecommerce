from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from app.models.models import Product_discount
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
                self.product_discount_repository.create(Product_discount(**discount.dict()))
        except:
            raise HTTPException(
                status_code=status.HTTP_403_UNAUTHORIZED, detail='Its only possible to create one discount by payment mode')