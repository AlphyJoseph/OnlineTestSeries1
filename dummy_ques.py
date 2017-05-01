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

##############################################################################
ques = Subjects(1,'Physics',"Before data can be transmitted, they must be transformed to ________.", "Periodic signals", "Electromagnetic signals","Aperiodic signals", "B")
session.add(ques)
ques = Subjects(2,'Physics','What is the speed of light?','3x10^8','djfb','sfkhs','3x10^8')
session.add(ques)
#############################################################################

session.commit()
session.commit()