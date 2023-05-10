from typing import Optional
from datetime import date
from pydantic import BaseModel


class ContactBase(BaseModel):
    name: str
    surname: str
    email: str
    phone: Optional[str] = None
    birthday: Optional[date] = None
    additional_data: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
