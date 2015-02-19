from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine
from sqlalchmey.orm import sessionmaker

Base=declarative_base()

class BeefyDatabase(object):
    def __init__(self, url):
        self.engine=create_engine(url, echo=True)
        self.Session=sessionmaker(bind=self.engine)
        self.session=self.Session()

    def add_person(self, **kwargs):
        person=Person(

class Person(Base):
    __tablename__ = 'person'
    idn=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    phone=Column(String)
    city=Column(String)
    state=Column(String)
    postal_code=Column(String)
    irc=Column(String)
    fb=Column(String)
    twitter=Column(String)
    interests=Column(String)
    email=Column(String)
    fas=Column(String)

    def __repr__(self):
        return 'Person(%s,%s,%s)' ( self.first_name, self.last_name,
                self.fas)

