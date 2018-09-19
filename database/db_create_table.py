#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 03:07:45 2018

@author: niveditanatarajan
"""
#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS JIVELY")

# Create table as per requirement
sql = """CREATE TABLE JIVELY (
   NAME  CHAR(20) NOT NULL,
   HUMIDITY INT,  
   TEMPERATURE FLOAT)"""

cursor.execute(sql)

# disconnect from server
db.close()
