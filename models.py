from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Boolean, Float, Text, Integer, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from config import config

engine = create_engine(config['sqlite'])
Base = declarative_base()


class Subway(Base):
    __tablename__ = 'subways'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    houses = relationship('House', back_populates='subway')

    def __repr__(self):
        return '<Subway {}>'.format(self.name)


class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True)
    number = Column(String(64))
    name = Column(String(64), index=True)
    area = Column(Float)
    price = Column(Integer)
    subway_distance = Column(String(64))
    url = Column(String(128))
    environment = Column(Text)
    traffic = Column(Text)

    subway_id = Column(Integer, ForeignKey('subways.id'))
    subway = relationship("Subway", back_populates='houses')

    def __repr__(self):
        return '<House {} {} {}>'.format(self.name, self.price, self.area)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
