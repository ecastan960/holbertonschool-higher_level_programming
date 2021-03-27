#!/usr/bin/python3
"""script that changes the name of a State object
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

if __name__ == '__main__':
    """This code its not executed if imported
    """
    username = argv[1]
    password = argv[2]
    d_name = argv[3]
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
    update = session.query(States).get(2)
    update.name = 'New Mexico'
    session.commit()
