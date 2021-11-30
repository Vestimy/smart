from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, DateTime, Column, DECIMAL, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from decimal import Decimal

# engine = create_engine('mysql+pymysql://root@localhost/new_test', echo=True)
engine = create_engine('mysql+pymysql://root@localhost/new_test')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String((16)))

    fullname = Column(String(16))
    nickname = Column(String(16))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    pcs = Column(Integer)
    price = Column(DECIMAL(15, 2))

    subcategoryequipmentid = Column(Integer, ForeignKey('subcategoryequipment.id'))
    subcategoryequipment = relationship('Equipment', back_populates='equipment')

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return self.title


class CategoryEquipment(Base):
    __tablename__ = 'categoryequipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, unique=True)
    description = Column(String(500))

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    subcategoryequipment = relationship('CategoryEquipment', back_populates='categoryequipment')

    def __repr__(self):
        return f'{self.id} {self.title} {self.description}'


class SubcategoryEquipment(Base):
    __tablename__ = 'subcategoryequipment'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(String(500))

    categoryequipmentid = Column(Integer, ForeignKey('categoryequipment.id'))
    categoryequipment = relationship('SubcategoryEquipment', back_populates='subcategoryequipment')

    equipment = relationship('SubcategoryEquipment', back_populates='subcategoryequipment')

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    city = Column()
    artist = Column()
    concert_hall = Column()
    executor = Column()
    note = Column()
    manager = Column()

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
