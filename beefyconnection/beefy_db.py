from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.orm import sessionmaker

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
        response = ""
        for value in queryResults:
          response += repr("<Person first_name=\"" + value.first_name + "\", last_name=\"" + value.last_name + "\", phone=\"" + value.phone + "\", city=\""+ value.city+"\", state=\""+ value.state+"\",postal_code=\""+ value.postal_code+"\",irc=\""+value.irc+"\",fb=\""+value.fb+"\",twitter=\""+value.twitter+"\",interests=\""+value.interests+"\",email=\""+value.email+"\",fas=\""+value.fas+"\"")
        return response

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
engine = create_engine('sqlite:///person.db', echo=True)
Base.metadata.create_all(engine)

