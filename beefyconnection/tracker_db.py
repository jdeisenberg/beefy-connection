from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Date, create_engine
from sqlalchmey.orm import sessionmaker

Base=declarative_base()

class BeefyDatabase(object):
    def __init__(self, url):
        self.engine=create_engine(url, echo=True)
        self.Session=sessionmaker(bind=self.engine)
        self.session=self.Session()

    def add_person(self, **kwargs):
        person=Person(**kwargs)
        self.session.add(person)
        self.session.commit()
    def read_person(self, **kwargs):
        queryResults = self.session.query(Person).all()
        for key, value in queryResults.iteritems():
          repr(key,"<Person first_name=\"",value["first_name"], "\", 
                            last_name=\"",value["last_name"],"\",
                            phone=\"",value["phone"],"\",
                            city=\"", value["city"],"\",
                            state=\"", value["city"],"\",
                            postal_code=\"", value["postal_code"],"\",
                            irc=\"",value["irc"],"\",
                            fb=\"",value["fb"],"\",
                            twitter=\"",value["twitter"],"\",
                            interests=\"",value["interests"],"\",
                            email=\"",value["email"],"\",
                            fas=\"",value["fas"],"\"")

class Person(Base):
    __tablename__ = 'person'
    id=Column(Integer, primary_key=True)
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

class Interests(Base):
    __tablename__ = 'interests'
    id=Column(Integer, primary_key=True)
    text=Column(String)

    def __repr__(self):
        return 'Interests(%s,%s)' ( self.id, self.text)

class Tracker(Base):
    __tablename__ = 'tracker'
    id=Column(Integer, primary_key=True)
    gate1=Date(Date)
    gate2=Date(Date)
    gate3=Date(Date)
    gate4=Date(Date)
    gate5=Date(Date)

    def __repr__(self):
        return 'Interests(%s,%s)' ( self.id, self.text)

