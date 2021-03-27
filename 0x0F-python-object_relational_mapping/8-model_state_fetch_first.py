#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

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

    session = Session(engine)
    count = 0
    if session.query(State.id).first() is None:
        print('Nothing')
    else:
        for state in session.query(State).order_by(State.id).all():
            if count == 0:
                print("{}: {}".format(state.id, state.name))
            count += 1
    session.close()
