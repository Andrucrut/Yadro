from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: uuid.UUID
    gender: str
    first_name: str
    last_name: str
    phone: str
    email: str
    city: str
    country: str
    picture: str