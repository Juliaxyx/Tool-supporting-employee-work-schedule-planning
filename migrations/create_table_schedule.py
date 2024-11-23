import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

connection = sqlite3.connect(db)
query = (''' CREATE TABLE SCHEDULE 
            (MAIN_EMPLOYEE           TEXT    NOT NULL,
            SUPPORT_EMPLOYEE           TEXT,
            DATE                TEXT    NOT NULL, 
            SHIFT               INTEGER NOT NULL
            );''') 
connection.execute(query)
connection.close()

#Zmiany: 
#1-rano
#2-popołudniu