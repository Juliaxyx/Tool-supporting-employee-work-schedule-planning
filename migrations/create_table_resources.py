import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

connection = sqlite3.connect(db)
query = (''' CREATE TABLE RESOURCES 
            (EMPLOYEE           TEXT    NOT NULL,
            DATE                TEXT    NOT NULL, 
            SHIFT               INTEGER NOT NULL, 
            MIN_H               INTEGER NOT NULL,
            MAX_H               INTEGER NOT NULL);''') 
connection.execute(query)
connection.close()

#Zmiany: 
#1-brak dostępności tego dnia
#2-dostępność na porannej zmianie
#3-dostępność na popołudniowej zmianie
#4-dostępność cały dzień