import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

#Dodawanie zadań
def insert_info(name, description, employee, priority, date_done, if_done):
    connection = sqlite3.connect(db)
    connection.execute("INSERT INTO TASKS (name, description, employee, priority, date_done, if_done) \
    VALUES (?,?,?,?,?,?)", (name, description, employee, priority, date_done, if_done))
    connection.commit()
    connection.close()

#Usuwanie zadań
def delete_info(name, date_done):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("DELETE from TASKS WHERE name = ? AND date_done = ?", (name, date_done))
    connection.commit()
    connection.close()

#Pozyskiwanie wartości z bazy danych 
def retrieve_info():
    results = []
    connection = sqlite3.connect(db)
    cursor = connection.execute("SELECT name, description, employee, priority, date_done, if_done from TASKS")
    for row in cursor:
        results.append(list(row))
    connection.close()  
    return results

#Aktualizacja zadań
def update_info(description, employee, if_done, name, date_done):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("UPDATE TASKS SET description = ?, employee = ?, IF_DONE = ? WHERE name = ? AND date_done = ?", (description, employee, if_done, name, date_done))
    connection.commit()
    connection.close()
    


   
    
