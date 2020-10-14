from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Recruit


engine = create_engine('postgresql+psycopg2://pguser:password@localhost:6543/development', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
     Recruit(first_name='A', surname='A', chatname='A',github_name='A@github',id_number=1,personal_email_address='A@gmail.com',cohort='C26 Data Eng'),
     Recruit(first_name='B', surname='B', chatname='B',github_name='B@github',id_number=2,personal_email_address='B@yahoo.com',cohort='C26 Data Eng'),
     Recruit(first_name='C', surname='C', chatname='C',github_name='C@github',id_number=3,personal_email_address='C@gmail.com',cohort='C26 Data Eng'),
     Recruit(first_name='D', surname='D', chatname='D',github_name='D@github',id_number=4,personal_email_address='D@yahoo.com',cohort='C26 Data Eng'),
     Recruit(first_name='E', surname='E', chatname='E',github_name='E@github',id_number=5,personal_email_address='E@personal.com',cohort='C26 Data Eng')])

session.commit()