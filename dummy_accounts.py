import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib, uuid
from DB_schemas import *
 
engine = create_engine('sqlite:///onlineTestSeries.db', echo=False)

salt = uuid.uuid4().hex
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()


#######################	One dummy user
dummyPassword = "al"
dummyUSN = "abc123"

hashed_password = hashlib.sha512(dummyPassword).hexdigest()
user = User(dummyUSN, hashed_password)
session.add(user)
#####################################33
 
# commit the record the database
session.commit()
session.commit()