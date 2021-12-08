from fastapi import Depends, HTTPException, status
from app.api.user.schemas import UserSchema
from app.repositories.customer_repository import CustomerRepository
from app.models.models import Customer, User
from app.api.customer.schemas import CreateCostumerSchema, CustomerSchema
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository = Depends(), user_service: UserService = Depends(), user_repository: UserRepository = Depends()):
        self.customer_repository = customer_repository
        self.user_service = user_service
        self.user_repository = user_repository

    def create(self, customer: CreateCostumerSchema):
        try:   
            self.user_service.create(UserSchema(display_name= "{} {}".format(customer.frist_name, customer.last_name), email = customer.email, password= customer.password,
            role = "customer" ))
        except:
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= "This email is alredy in use.")

        id = self.user_repository.find_by_email(customer.email).id
        self.customer_repository.create(Customer( frist_name = customer.frist_name, last_name  = customer.last_name, phone_number = customer.phone_number,
        genre = customer.genre, document_id = customer.document_id , birth_date = customer.birth_date , user_id= id ))

