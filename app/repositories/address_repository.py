from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Adresses
from .base_repository import BaseRepository

class AdressRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Adresses)

    def get_by_customer_id(self, customer_id):
        return self.session.query(Adresses).filter_by(customer_id = customer_id).all()