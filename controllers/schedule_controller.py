import datetime
import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

#    
#    
#     
def insert_info(employee, month, shifts, min_h, max_h):
    connection = sqlite3.connect(db)
    print(employee, month, shifts, min_h, max_h)
    for index, shift in enumerate(shifts):
        date = str(index+1) + '/' + str(month+1) + '/' + str(datetime.datetime.now().year)
        connection.execute("INSERT INTO SCHEDULE (EMPLOYEE, DATE, SHIFT, MIN_H, MAX_H) \
        VALUES (?,?,?,?,?)", (employee, date, int(shift), int(min_h), int(max_h)))
        connection.commit()
    connection.close()  
   
#    
#    
#     
def update_info(employee, month, shifts, min_h, max_h):
    connection = sqlite3.connect(db)
    print(employee, month, shifts, min_h, max_h)
    for index, shift in enumerate(shifts):
        date = str(index+1) + '/' + str(month+1) + '/' + str(datetime.datetime.now().year)
        connection.execute("UPDATE SCHEDULE SET SHIFT = ?, MIN_H = ?, MAX_H = ? WHERE EMPLOYEE = ? AND DATE = ?", 
                           (int(shift), int(min_h), int(max_h), employee, date))
        connection.commit()
    connection.close() 

def retrieve_info_form(month):
    results = []
    connection = sqlite3.connect(db)
    cursor = connection.execute("SELECT * FROM RESOURCES WHERE DATE LIKE '%/" + str(month+1) + "/" + str(datetime.datetime.now().year) + "%'")
    for row in cursor:
        results.append(list(row))
    connection.close()  
    return results

def retrieve_info_schedule(month):
    results = []
    connection = sqlite3.connect(db)
    cursor = connection.execute("SELECT * FROM SCHEDULE WHERE DATE LIKE '%/" + str(month+1) + "/" + str(datetime.datetime.now().year) + "%'")
    for row in cursor:
        results.append(list(row))
    connection.close()  
    return results

