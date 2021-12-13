from fastapi import Depends, HTTPException, status
import uuid
from app.api.order.schemas import OrderSchema
from app.models.models import Order
from app.models.models import OrderProducts
from app.repositories.customer_repository import CustomerRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.coupons_repository import CouponsRepository
from app.repositories.order_product_repository import OrderProductsRepository
from .auth_service import get_user
from enum import Enum
from datetime import datetime


class OrderStatus(str, Enum):
    ORDER_PLACED = "ORDER_PLACED"
    ORDED_PAID = "ORDER_PAID"
    ORDER_SHIPPED = "ORDER_SHIPPED" 
    ORDER_RECEIVED = "ORDER_RECEIVED"
    ORDER_COMPLETED = "ORDER_COMPLETED"
    ORDER_CANCELLED = "ORDER_CANCELLED"

class OrderService:
    def __init__(self, order_repository: OrderRepository = Depends(),product_repository: ProductRepository = Depends(),
                coupon_repository: CouponsRepository = Depends(), user: get_user = Depends(), customer_repository: CustomerRepository = Depends(),
                order_product_repository: OrderProductsRepository = Depends()):
        self.order_repository = order_repository
        self.product_repository = product_repository
        self.coupon_repository = coupon_repository
        self.get_user = user
        self.customer_repository = customer_repository
        self.order_product_repository = order_product_repository

    def create(self, order: OrderSchema):
        number = uuid.uuid4().int
        status = OrderStatus.ORDER_PLACED
        customer_id =  self.customer_repository.get_by_user_id(get_user().id)
        created_at = datetime.now()
        address_id = order.address_id
        total_value = self.calc_total(order)
        payment_form_id = order.payment_method_id
        total_discount = self.calc_discount(total_value, payment_form_id, order.coupon_code)

        try: 
            id = self.order_repository.create(Order( number = number, status = status, customer_id = customer_id , created_at = created_at,
                                    address_id = address_id, total_value= total_value, payment_form_id = payment_form_id, 
                                    total_discount = total_discount))
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Order creation Failed')

        self.create_orders(order, id)

    def create_ordes(self, orders, id):
        for order in orders.products:
            self.order_product_repository.create(order_id = id , product_id = order.id , quantity= order.quantity)
            
    def calc_total(self, order: OrderSchema) -> float :
        products = order.products
        total = 0.0

        for product  in products:
            total  += self.product_repository.get_by_id(product.id).price * product.quantity
        
        return total
    
    def calc_discount(self, total_value: float, payment_form_id: int, coupon_code) -> float:
        total_discount = 0.0
        if coupon_code :
            coupon = self.coupon_repository.get_by_code(coupon_code)
            if (coupon.expire_at <  datetime.now()) and (coupon.limit > 0):
                total_discount = coupon.value
                self.coupon_repository.update(coupon.id, {"limit": coupon.limit - 1})

        return total_discount*total_value        