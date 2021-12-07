from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Adresses
from app.repositories.address_repository import AdressRepository
from app.services.address_service import AddressService
from .schemas import AddressSchema, ShowAddressSchema

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(address: AddressSchema, service: AddressService = Depends()):
    service.create(address)

@router.get('/', response_model=List[ShowAddressSchema])
def index(repository: AdressRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, address: AddressSchema, repository: AdressRepository = Depends()):
    repository.update(id, address.dict())

@router.get('/{id}', response_model=ShowAddressSchema)
def show(id: int, repository: AdressRepository = Depends()):
    return repository.get_by_id(id)
