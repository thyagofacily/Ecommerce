from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Customer
from app.repositories.customer_repository import CustomerRepository
from .schemas import CustomerSchema, ShowCustomerSchema ,CustomerUpdateSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(customer: CustomerSchema, repository: CustomerRepository = Depends()):
    repository.create(Customer(**customer.dict()))


@router.get('/', response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, customer: CustomerUpdateSchema, repository: CustomerRepository = Depends()):
    repository.update(id, customer.dict())


@router.get('/{id}', response_model=ShowCustomerSchema)
def show(id: int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)
