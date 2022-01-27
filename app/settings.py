from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
  db_username: str ="thyagopereira"
  db_password: str = "123"
  db_name: str = "postgress"
  db_port: int = "3001"

  @property
  def db_url(self):
    print(f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}')
    return f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}'

settings = Settings()
