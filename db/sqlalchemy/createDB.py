#!/usr/bin/python2.7
from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Person(Base):
    #Name of table
    __tablename__ = "person"

    #Attributes of table
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    organization = Column(String)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    language = Column(String)
    irc = Column(String)
    fb = Column(String)
    twitter = Column(String)

#Use sqlite engine and create table
engine = create_engine('sqlite:///images.db', echo=True)
Base.metadata.create_all(engine)

