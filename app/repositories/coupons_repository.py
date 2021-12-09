from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Coupons
from .base_repository import BaseRepository

class CouponsRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Coupons)

    def get_by_code(self, code):
        return self.session.query(self.model).filter_by(code=code).first()

    