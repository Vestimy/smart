from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, DateTime, Column, DECIMAL, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from decimal import Decimal

from test2 import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    pcs = Column(Integer)
    price = Column(DECIMAL(15, 2))

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return self.title

    def load_all(self):
        try:
            result = Equipment.query.all()
            return result
        except Exception as e:
            print(e)

    def save(self, title, pcs, price):
        try:
            new = Equipment(title=title, pcs=int(pcs), price=Decimal(price))
            session.add(new)
            session.commit()
        except Exception as e:
            session.rollback()


class CategoryEquipment(Base):
    __tablename__ = 'categoryequipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, unique=True)
    description = Column(String(500))

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def save_category(self, title, description=None):
        try:
            category = СategoryEquipment(title=title, description=description)
            session.add(category)
            session.commit()
            return (True, "Its OK")
        except IntegrityError as e:
            session.rollback()
            return (False, e)

    def update_title(self, id, title=None, description=None):
        error = ''
        try:
            object = СategoryEquipment.query.get(id)
            if title is not None:
                object.title = title
            if description is not None:
                object.description = description
            session.commit()
            return (True, error, object)
        except IntegrityError as e:
            session.rollback()
            return (False, e, object)

    def delete_category(self, id):
        id = int(id)
        res = СategoryEquipment.query.get(id)
        session.delete(res)
        session.commit()
        session.close()
        return True

    @classmethod
    def load_all_category(cls):
        category = cls.query.all()
        count = cls.query.count()
        return (category, count)

    @classmethod
    def search_id(cls, title):
        result = cls.query.filter(СategoryEquipment.title == title).one()
        return result.id

    @classmethod
    def load_subcategory(cls):
        return cls.query.all()

    def __repr__(self):
        return f'{self.id} {self.title} {self.description}'


class SubcategoryEquipment(Base):
    __tablename__ = 'subcategoryequipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(String(500))

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_onupdate=func.now())
