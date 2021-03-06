#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 03:12:24 2018

@author: niveditanatarajan
"""
import pymysql
import sqlalchemy
import pyodbc
#!/usr/bin/python3
'''
import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO JIVELY
            (NAME, HUMIDITY, TEMPERATURE)
   VALUES ('Niv', 20, 30)""" #change to values generated by temp.py
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
'''
def sqlinsert(UID,NAME):
    db=pymysql.connect("localhost","testuser","test123","TESTDB")
    cursor=db.cursor()
   
    UID=UID+1
    #UID = fList[0][0];NAME=fList[0][1]
    #queryInsertStudentTable = """CREATE TABLE JIVELY (UID INT, NAME varchar(25) not null)"""

    #cursor.execute(queryInsertStudentTable)
    '''
    sql = """CREATE TABLE JIVELY (
                UID INT,
                NAME varchar(25) not null)"""
    cursor.execute(sql)
    '''
    queryInsert = "INSERT INTO JIVELY (UID,NAME) VALUES (%s,%s)"
    val=(UID,NAME)
    #Generate multiple values from the list to be placed in a query
   
    
    try:
        cursor.execute(queryInsert,val)
        print("record inserted")
        db.commit()
    except:
        db.rollback()
    
    db.close()