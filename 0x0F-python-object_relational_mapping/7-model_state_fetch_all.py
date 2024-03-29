#!/usr/bin/python3
"""Module list all state objects from a db
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
             'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                 sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
