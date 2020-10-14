from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Recruit


engine = create_engine('postgresql+psycopg2://pguser:password@localhost:6543/production', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
     Recruit(first_name='F', surname='A', rocketchat_user='F',github_name='F@github',personal_email_address='FF@gmail.com',cohort='C28 Data Eng'),
     Recruit(first_name='G', surname='G', rocketchat_user='G',github_name='G@github',personal_email_address='GF@yahoo.com',cohort='C28 Data Eng'),
     Recruit(first_name='H', surname='H', rocketchat_user='H',github_name='H@github',personal_email_address='HF@gmail.com',cohort='C28 Data Eng'),
     Recruit(first_name='I', surname='I', rocketchat_user='I',github_name='I@github',personal_email_address='IF@yahoo.com',cohort='C28 Data Eng'),
     Recruit(first_name='J', surname='J', rocketchat_user='J',github_name='J@github',personal_email_address='JF@personal.com',cohort='C28 Data Eng')])

session.commit()