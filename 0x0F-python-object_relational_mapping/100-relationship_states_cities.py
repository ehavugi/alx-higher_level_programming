#!/usr/bin/python3
""" Create state "California" and a city "San Francisco" in California
"""
import sys
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City, Base
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)

    session = scoped_session(sessionmaker(bind=engine))

    ca = State(name="California")
    sf = City(name="San Francisco", state=ca)
    session.add(ca)
    session.add(sf)
    session.commit()

    session.close()
