from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///onlineTestSeries.db', echo=True)
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
class Subjects(Base)

	__tablename__="sub_questions"

	qno = Column(Integer, primary_key=True)
	sub = Column(String, primary_key=True)
	que = Column(String)
	op1 = Column(String)
	op2 = Column(String)
	op3 = Column(String)
	ans = Column(String)

	def __init__(self, qno, sub, que, op1, op2, op3, ans):

		self.qno = qno
		self.sub = sub
		self.que = que
		self.op1 = op1
		self.op2 = op2
		self.op3 = op3
		self.ans = ans
########################################################################

##  Add other Table schemas as Classes
#   Refer above (User) schema
class Semester(Base):
	""""""
	__tablename__ = "sem_subjects"

	sem = Column(Integer, primary_key=True)
	subjects = Column(String)

	def __init__(self, sem, subjects):
		self.sem = sem
		self.subjects = subjects


		
########################################################################
#   *** Do not change the below line ***
# create tables
Base.metadata.create_all(engine)