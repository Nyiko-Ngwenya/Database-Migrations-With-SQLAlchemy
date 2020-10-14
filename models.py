# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/
# engine = create_engine('sqlite:///dev.db', echo=True) "postgresql+psycopg2://user:password@/dbname"
Base = declarative_base()

class Recruit(Base):
    __tablename__ = 'recruits'
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    rocketchat_user = Column(String)
    github_name = Column(String)
    # id_number = Column(Integer)
    personal_email_address = Column(String,nullable=False,unique=True)
    cohort = Column(String,server_default="C25 Data Eng",default="C25 Data Eng",nullable=False)
