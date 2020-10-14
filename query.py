from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://pguser:password@localhost:6543/development', echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from models import Recruit

for row in session.query(Recruit,Recruit.first_name):
    print(row.Recruit,row.first_name)