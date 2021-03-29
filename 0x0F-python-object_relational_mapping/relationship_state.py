#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class that defines states inside the database

    Args:
        Base ([type]): Inherited class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates="states", cascade="all, delete, delete-orphan")
