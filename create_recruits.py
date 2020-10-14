from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Recruit


engine = create_engine('postgresql+psycopg2://pguser:password@localhost:6543/development', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
     Recruit(first_name='Wendy', surname='Williams', chatname='windy',github_name='windy@github',id_number=123456789,personal_email_address='windy@gmail.com'),
     Recruit(first_name='Mary', surname='Contrary', chatname='mary',github_name='mary@github',id_number=134679258,personal_email_address='windy@yahoo.com'),
     Recruit(first_name='Fred', surname='Flintstone', chatname='freddy',github_name='freddy@github',id_number=159258357,personal_email_address='windy@personal.com')])

session.commit()