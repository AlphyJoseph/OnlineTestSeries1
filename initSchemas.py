import sqlite3

conn = sqlite3.connect('onlinetestseries.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE USERS
       (USN 	TEXT    PRIMARY KEY	NOT NULL,
       PASSWORD	INT     NOT NULL);
       ''')

print "USER Table created successfully"

conn.close()