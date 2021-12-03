from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Coupons
from app.repositories.coupons_repository import CouponsRepository
from .schemas import CouponSchema, ShowCouponSchema, EditCouponSchema

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponsRepository = Depends()):
    repository.create(Coupons(**coupon.dict()))

@router.get('/', response_model=List[ShowCouponSchema])
def index(repository: CouponsRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, coupon: EditCouponSchema, repository: CouponsRepository = Depends()):
    repository.update(id, coupon.dict())

@router.get('/{id}', response_model=ShowCouponSchema)
def show(id: int, repository: CouponsRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}')
def delete(id: int, repository: CouponsRepository = Depends()):
    return repository.delete(id)
