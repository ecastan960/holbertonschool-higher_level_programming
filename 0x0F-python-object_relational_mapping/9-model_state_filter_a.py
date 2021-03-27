#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

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

    session = Session(engine)
    q = session.query(State).order_by(State.id).filter(State.name.like('%a%'))
    for state in q:
        print("{}: {}".format(state.id, state.name))
    session.close()
