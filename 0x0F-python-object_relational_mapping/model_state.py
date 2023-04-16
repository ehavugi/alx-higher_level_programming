from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql 

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(mysql.INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128), nullable=False)
