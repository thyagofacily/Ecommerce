from pydantic import BaseModel
from app.api.customer.schemas import ShowCustomerSchema

class AddressSchema(BaseModel):
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: int
    customer_id: int

class ShowAddressSchema(AddressSchema):
    id: int 
    customer : ShowCustomerSchema

    class Config:
        orm_mode = True
