from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :

class Offer(Base):
    __tablename__ = "offers"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    ingredients= Column(String)
    comment=relationship("Comment", back_populates="offer") 



    def __repr__(self):
        return ("Offer name: {}".format(self.name))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name=Column(String)
    username=Column(String, unique=True)
    password=Column(String)
    comment=relationship("Comment", back_populates="user") 
   
   
    def __repr__(self):
        return ("User name: {}".format(self.name))

class Comment(Base):
    __tablename__="comments"
    id=Column(Integer, primary_key = True)
    text=Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="comment")
    offer_id=Column(Integer, ForeignKey('offers.id'))
    offer= relationship("Offer", back_populates="comment")