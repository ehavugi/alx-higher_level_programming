#!/usr/bin/python3
"""Create table named states in sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
    State class. Starter class for interacting states table.
    in MYSQL db
    """
    __tablename__ = 'states'
    id = Column(mysql.INTEGER(11), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")
