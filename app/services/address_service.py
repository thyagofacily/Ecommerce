from fastapi import Depends
from app.repositories.address_repository import AdressRepository
from app.repositories.customer_repository import CustomerRepository
from app.api.address.schemas import AddressSchema
from app.models.models import Adresses


class AddressService:
    def __init__(self, address_repository:  AdressRepository = Depends(), customer_repository: CustomerRepository = Depends()):
        self.address_repository = address_repository
        self.customer_repository = customer_repository

    def create(self, address : AddressSchema):
        #Se ja houver endereço primário para o mesmo Customer
        if address.primary == 1:
            addreses = self.address_repository.get_by_customer_id(address.customer_id)
            for ad in addreses:
                if ad.primary == 1:
                    ad.primary = 0
                     
        self.address_repository.create(Adresses(**address.dict()))          

        

