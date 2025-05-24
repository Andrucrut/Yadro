from pydantic import BaseModel
from uuid import UUID


class UserCreate(BaseModel):
    uuid: UUID
    gender: str
    first_name: str
    last_name: str
    phone: str
    email: str
    city: str
    country: str
    picture: str


class UserRead(UserCreate):
    id: int