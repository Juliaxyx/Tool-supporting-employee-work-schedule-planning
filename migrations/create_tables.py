import sqlite3

def resources(db):
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

def schedule(db):
    connection = sqlite3.connect(db)
    query = (''' CREATE TABLE SCHEDULE 
                (MAIN_EMPLOYEE      TEXT   NOT NULL,
                SUPPORT_EMPLOYEE    TEXT,
                DATE                TEXT    NOT NULL, 
                SHIFT               INTEGER NOT NULL
                );''') 
    connection.execute(query)
    connection.close()
    
#Zmiany: 
#1-rano
#2-popołudniu

def tasks(db):
    connection = sqlite3.connect(db)
    query = (''' CREATE TABLE TASKS
                (NAME           TEXT    NOT NULL,
                DESCRIPTION     TEXT, 
                EMPLOYEE        TEXT,
                PRIORITY        TEXT,
                DATE_DONE       DATE    NOT NULL,
                IF_DONE         TEXT    NOT NULL);''') 
    connection.execute(query)
    connection.close()
    