from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
from app.settings import settings

DB_PATH = Path(__file__).resolve().parent

SQLALCHEMY_DATABASE_URL = settings.db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

metadata = Base.metadata


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
