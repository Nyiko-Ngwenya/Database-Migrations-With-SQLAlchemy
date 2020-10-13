from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Recruit(Base):
    __tablename__ = 'recruits'

    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    chatname = Column(String)
    github_name = Column(String)
    id_number = Column(Integer)
