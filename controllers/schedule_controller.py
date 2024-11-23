import datetime
import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '../databases/resources.db')

#    
#    
#     
def insert_info(days, month):
    connection = sqlite3.connect(db)
    for index, day in enumerate(days):
        date = str(index+1) + '/' + str(month+1) + '/' + str(datetime.datetime.now().year)
        connection.execute("INSERT INTO SCHEDULE (MAIN_EMPLOYEE, SUPPORT_EMPLOYEE, DATE, SHIFT) \
        VALUES (?,?,?,?)", (day[0], day[1], date, 1))
        connection.execute("INSERT INTO SCHEDULE (MAIN_EMPLOYEE, SUPPORT_EMPLOYEE, DATE, SHIFT) \
        VALUES (?,?,?,?)", (day[2], day[3], date, 2))
        connection.commit()
    connection.close()  
   
#    
#    
#     
def update_info(days, month):
    connection = sqlite3.connect(db)
    for index, day in enumerate(days):
        date = str(index+1) + '/' + str(month+1) + '/' + str(datetime.datetime.now().year)
        connection.execute("UPDATE SCHEDULE SET MAIN_EMPLOYEE = ?, SUPPORT_EMPLOYEE = ? WHERE DATE = ? AND SHIFT = ?", (day[0], day[1], date, 1))
        connection.execute("UPDATE SCHEDULE SET MAIN_EMPLOYEE = ?, SUPPORT_EMPLOYEE = ? WHERE DATE = ? AND SHIFT = ?", (day[2], day[3], date, 2))
        connection.commit()
    connection.close() 


def retrieve_info_form(month):
    results = {}
    connection = sqlite3.connect(db)
    cursor = connection.execute("SELECT * FROM RESOURCES WHERE DATE LIKE '%/" + str(month+1) + "/" + str(datetime.datetime.now().year) + "%'")
    for row in cursor:
        record = list(row)
        if results.get(record[0]) != None:
            results[record[0]]['days'][record[1][0:record[1].find('/')]] = record[2]
        else:
            results[record[0]] = {'days': {record[1][0:record[1].find('/')]: record[2]}, 'min': record[3], 'max': record[4]}
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

