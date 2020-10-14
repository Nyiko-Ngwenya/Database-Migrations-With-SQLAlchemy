from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Recruit


engine = create_engine('postgresql+psycopg2://pguser:password@localhost:6543/production', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
     Recruit(first_name='F', surname='A', rocketchat_user='F',github_name='F@github',id_number=11,personal_email_address='F@gmail.com',cohort='C27 Data Eng'),
     Recruit(first_name='G', surname='G', rocketchat_user='G',github_name='G@github',id_number=22,personal_email_address='G@yahoo.com',cohort='C27 Data Eng'),
     Recruit(first_name='H', surname='H', rocketchat_user='H',github_name='H@github',id_number=33,personal_email_address='H@gmail.com',cohort='C27 Data Eng'),
     Recruit(first_name='I', surname='I', rocketchat_user='I',github_name='I@github',id_number=44,personal_email_address='I@yahoo.com',cohort='C27 Data Eng'),
     Recruit(first_name='J', surname='J', rocketchat_user='J',github_name='J@github',id_number=55,personal_email_address='J@personal.com',cohort='C27 Data Eng')])

session.commit()