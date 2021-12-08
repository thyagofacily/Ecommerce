from fastapi import APIRouter
from fastapi.param_functions import Depends
from typing import List
from app.repositories.user_repository import UserRepository
from .schemas import UserSchema, ShowUserSchema
from app.models.models import User
from app.services.user_service import UserService

router = APIRouter()

@router.post('/')
def create(user: UserSchema, service: UserService =  Depends()):
    service.create(user)

@router.get('/', response_model=List[ShowUserSchema])
def index(repository: UserRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, user: UserSchema, service: UserService = Depends()):
    service.update(id, user)

@router.get('/{id}', response_model=ShowUserSchema)
def show(id: int, repository: UserRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}')
def delete(id: int, repository: UserRepository = Depends()):
    repository.delete(id)

