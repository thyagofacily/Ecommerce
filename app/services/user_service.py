from fastapi import Depends , HTTPException, status
from app.repositories.user_repository import UserRepository
from app.models.models import User
from app.api.user.schemas import UserSchema
import bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository = Depends()) :
        self.user_repository = user_repository
    
    def create(self, user: UserSchema):

        if self.user_repository.find_by_email(user.email):
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= "This email is alredy in use.")
        else:
            user.password = bcrypt.hashpw(
            user.password.encode('utf8'), bcrypt.gensalt())
            self.user_repository.create(User(**user.dict()))
        