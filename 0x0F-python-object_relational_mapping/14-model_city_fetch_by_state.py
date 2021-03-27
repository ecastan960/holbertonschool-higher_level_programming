#!/usr/bin/python3
"""script that deletes all State objects with a
name containing the letter a from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
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
    query = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id.asc()).all()

    for cities, states in query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    session.close()
