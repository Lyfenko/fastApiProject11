from sqlalchemy import Column, Integer, String, Date
from database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    surname = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    phone = Column(String(20))
    birthday = Column(Date)
    additional_data = Column(String(200))
