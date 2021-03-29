#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, MetaData, Table
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
    session = Session(engine)
    s1 = State(name='California')
    c1 = City(name='San Francisco')
    s1.cities.append(c1)
    session.add_all()
    session.commit()
    session.close()
