from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add(name, password):
	me= User(
		name=name,
		password= password)
	session.add(me)
	session.commit()

def check(name,password):
	user = session.query(
		User).filter_by(
       name=name).first()
	if user.password== password:
		return True
	else:
		return False

def users():
	return session.query(User).all()


print(users()[0].password)