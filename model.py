from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Participants(Base):
	__tablename__ = "#"
	costumer_id = Column(Integer , primary_key=True)
	name = Column(String)
	email = Column(String)
	pet = Column(String)