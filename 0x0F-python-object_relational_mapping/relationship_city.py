#!/usr/bin/python3
"""script that contains class definition of a city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import State

Base = declarative_base()


class City(Base):
    """Class that defines cities inside the database

    Args:
        Base ([type]): Inherited class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
