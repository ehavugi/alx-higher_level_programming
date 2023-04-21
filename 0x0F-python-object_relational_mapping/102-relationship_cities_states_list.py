#!/usr/bin/python3
""" update State object with state.id 2 to New Mexico
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state, in cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))