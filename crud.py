from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from datetime import date, timedelta

import models
import schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(
        name=contact.name,
        surname=contact.surname,
        email=contact.email,
        phone=contact.phone,
        birthday=contact.birthday,
        additional_data=contact.additional_data
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()


def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).get(contact_id)


def update_contact(db: Session, db_contact: models.Contact, contact: schemas.ContactUpdate):
    for field in contact.dict(exclude_unset=True):
        setattr(db_contact, field, contact.dict()[field])
    db.commit()
    db.refresh(db_contact)
    return db_contact


def delete_contact(db: Session, db_contact: models.Contact):
    db.delete(db_contact)
    db.commit()
    return db_contact


def search_contacts(db: Session, query: str):
    query = f"%{query}%"
    return db.query(models.Contact).filter(
        or_(
            func.lower(models.Contact.name).ilike(func.lower(query)),
            func.lower(models.Contact.surname).ilike(func.lower(query)),
            func.lower(models.Contact.email).ilike(func.lower(query))
        )
    ).all()


def get_upcoming_birthdays(db: Session):
    today = date.today()
    next_week = today + timedelta(days=7)
    return db.query(models.Contact).filter(
        and_(
            func.extract('month', models.Contact.birthday) == today.month,
            func.extract('day', models.Contact.birthday) >= today.day,
            func.extract('day', models.Contact.birthday) <= next_week.day
        )
    ).all()
