import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Boolean, Float, Text, Integer, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

basedir = os.path.abspath(os.path.dirname(__name__))
engine = create_engine('sqlite:///{}/test.data'.format(basedir))
Base = declarative_base()


class Subway(Base):
    __tablename__ = 'subways'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    houses = relationship('House', back_populates='subway')

    def __repr__(self):
        return '<Subway {}>'.format(self.name)


class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    name = Column(String, index=True)
    area = Column(Float)
    price = Column(Integer)
    subway_distance = Column(String)
    url = Column(String)
    environment = Column(Text)
    traffic = Column(Text)

    subway_id = Column(Integer, ForeignKey('subways.id'))
    subway = relationship("Subway", back_populates='houses')

    def __repr__(self):
        return '<House {} {} {}>'.format(self.name, self.price, self.area)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
