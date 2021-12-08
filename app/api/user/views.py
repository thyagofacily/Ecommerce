from fastapi import APIRouter
from fastapi.param_functions import Depends
from .schemas import UserSchema
from app.models.models import User
from app.services.user_service import UserService

router = APIRouter()


@router.post('/')
def create(user: UserSchema, service: UserService =  Depends()):
    service.create(user)
    