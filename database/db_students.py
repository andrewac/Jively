#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 02:05:46 2018

@author: niveditanatarajan
"""
import pymysql
def sql_insert():
    
    f=open(r"data1.csv","r")
    fstring = f.read()

    fList=[]
    for line in fstring.split('\n'):
        fList.append(line.split(','))
        #print(fList)

    db = pymysql.connect("localhost","testuser","test123","TESTDB")

    #prepare cursor
    cursor = db.cursor()

    #define drop tabel for cursor
    cursor.execute("DROP TABLE IF EXISTS JIVELYDATA")

    #create column names from first line
    UID=fList[0][0];HUMIDITY = fList[0][1];TEMPERATURE=fList[0][2];

    #query to generate table with the above column names
    queryCreateStudentTable = """CREATE TABLE JIVELYDATA(
                            {} int,
                            {} int,
                            {} float
                            )""".format(UID,HUMIDITY,TEMPERATURE)

    cursor.execute(queryCreateStudentTable)

    del fList[0]
    #Generate multiple values from the list to be placed in a query
    rows = ''
    for i in range(len(fList) - 1):
        rows += "('{}','{}','{}')".format(fList[i][0],fList[i][1],fList[i][2])
        if i != len(fList) - 2:
            rows += ','
        
    #print(rows)
    #print(rows) //used to make sure the last value is not a comma
    queryInsert="INSERT INTO JIVELYDATA VALUES"+rows
    try:
    #execute sql command
        cursor.execute(queryInsert)
    #comit changes to the database
        db.commit()
    except:
    #rollback in case there is any errors
        db.rollback()
    db.close() 