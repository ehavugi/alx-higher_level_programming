#!/usr/bin/env python3
""" First module ORM for MYSQL
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
if __name__ == "__main__":
    if len(sys.argv)>=4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,pwd, db), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        engine.connect()
        print(engine.table_names())

        Session =  sessionmaker(bind=engine)
        session = Session()
        """for state in session.query().all(): # HERE: no SQL query, only objects!
            print("{}:".format(state))"""
        session.close()
