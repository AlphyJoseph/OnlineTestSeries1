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
semes = semester(2,'Physics,Electrical,Civil','{{url_for(phy)}},{{url_for(ele)}},{{url_for(civ)}}')
session.add(semes)
#####################################33
 
# commit the record the database
session.commit()
session.commit()