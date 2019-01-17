from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_offer(name,ingredients):
    offer_object=Offer(
    	name=name,
    	ingredients=ingredients)
    session.add(offer_oject)
    session.commit()

def query_by_name(name):
    return session.query(Offer).filter(Offer.name.contains(name))

def add_user(first_name, last_name, username, password, ):	
    user_object = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password)

    session.add(user_object)
    session.commit()

def add_comment(text, user, offer):
    comment_object = Comment(
        text=text,
        user=user,
        offer=offer)

    session.add(comment_object)
    session.commit()  

def query_by_username(username):
    return session.query(User).filter_by(
        username=username).first()

def query_all():
	offers = session.query(Offer).all()
	return offers

def delete_comment_by_id(comment_id):
    session.query(Comment).filter_by(
        id=comment_id).delete()

    session.commit()
