import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

connection = sqlite3.connect(db)
query = (''' CREATE TABLE TASKS
            (NAME           TEXT    NOT NULL,
            DESCRIPTION     TEXT, 
            EMPLOYEE        TEXT,
            PRIORITY        TEXT,
            DATE_DONE       DATE,
            IF_DONE         TEXT);''') 
connection.execute(query)
connection.close()