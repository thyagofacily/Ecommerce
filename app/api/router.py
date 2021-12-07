from fastapi import APIRouter
from .product.views import router as product_router
from .category.views import router as category_router
from .supplier.views import router as supplier_router
from .payment_method.views import router as payment_method_router
from .product_discount.views import router as discount_router
from .coupons.views import router as coupons_router
from .customer.views import router as customer_router
from .address.views import router as address_router
from .user.views import router as user_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(category_router, prefix='/categories', tags=['category'])
router.include_router(supplier_router, prefix='/suppliers', tags=['supplier'])
router.include_router(
    discount_router, prefix='/product-discounts', tags=['product-discount'])
router.include_router(payment_method_router,
                      prefix='/payment-methods', tags=['payment-method'])

router.include_router(coupons_router, prefix='/coupons', tags=['coupons'])
router.include_router(customer_router, prefix='/customer', tags=["customer"])
router.include_router(address_router, prefix="/address", tags=["address"])
router.include_router(user_router, prefix='/users', tags=['users'])