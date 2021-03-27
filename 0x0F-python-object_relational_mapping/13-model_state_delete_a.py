#!/usr/bin/python3
"""script that deletes all State objects with a
name containing the letter a from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy import delete

username = argv[1]
password = argv[2]
d_name = argv[3]

if __name__ == '__main__':
    """This code its not executed if imported
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, d_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    class States(Base):
        __tablename__ = 'states'
        __table_args__ = {'extend_existing': True}

        id = Column(Integer, primary_key=True)
        name = Column(String)

    session = Session(engine)
    del1 = session.query(States).filter(State.name.like('%a%'))
    for state in del1:
        session.delete(state)
    session.commit()
