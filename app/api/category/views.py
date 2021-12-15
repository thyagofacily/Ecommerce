from typing import List
from fastapi import APIRouter, status, Depends

from app.repositories.category_repository import CategoryRepository
from .schemas import CategorySchema, ShowCategorySchema
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.models.models import Category
from app.services.auth_service import get_user, only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema, repository: CategoryRepository = Depends()):
    return repository.create(Category(**category.dict()))
    
@router.get('/', response_model=List[ShowCategorySchema])
def index(repository: CategoryRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, category: CategorySchema, repository: CategoryRepository = Depends()):
    return repository.update(id, category.dict())

@router.get('/{id}', response_model=ShowCategorySchema)
def show(id: int, repository: CategoryRepository = Depends()):
    return repository.get_by_id(id)
