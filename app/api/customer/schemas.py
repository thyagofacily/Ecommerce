from pydantic import BaseModel
from datetime import date

class CustomerSchema(BaseModel):
    frist_name : str
    last_name : str
    phone_number: str
    genre : str
    document_id : str
    birth_date : date

class CreateCostumerSchema(CustomerSchema):
    email:str
    password:str
    
    class Config:
        orm_mode = True

class CustomerUpdateSchema(BaseModel):
    frist_name : str
    last_name : str
    phone_number: str
    genre: str
    birth_date: date

class ShowCustomerSchema(CustomerSchema):
    id : int 

    class Config:
        orm_mode = True