from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///onlineTestSeries.db', echo=False)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    usn = Column(String, primary_key=True)
    password = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, usn, password):
        """"""
        self.usn = usn
        self.password = password
 

########################################################################

##  Add other Table schemas as Classes
#   Refer above (User) schema





########################################################################
#   *** Do not change the below line ***
# create tables
Base.metadata.create_all(engine)