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
semes = Semester(1,'Engineering Mathematics-1,Physics,Civil, Mechanical, Electrical,')
session.add(semes)
semes = Semester(2,'Engineering Mathematics-2,Chemistry,Programming in C,Electronics')
session.add(semes)
semes = Semester(3,'Engineering Mathematics-3,Electronic Circuits,Logic Design, Discrete Mathematical Structures,Data Structures with C, OOP with C++')
session.add(semes)
semes = Semester(4,'Engineering Mathematics-4, Graph Theory, ADA, Unix and Shell Programming, Microprocessors, Computer Organization')
session.add(semes)
semes = Semester(5,'Software Engineering, System Software, Operating Systems, DBMS, FLAT,Computer Networks-1')
session.add(semes)
semes = Semester(6,'Management & Entrepreneurship,Unix System Programming,Compiler Design, Computer Networks-2,Computer Graphics, Operations Research,Pattern Recognition')
session.add(semes)
#####################################33
 
# commit the record the database
session.commit()
session.commit()