#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 02:05:46 2018

@author: niveditanatarajan
"""

import pymysql
f=open(r"data1.csv","r")
fstring = f.read()

fList=[]
for line in fstring.split('\n'):
    fList.append(line.split(','))
print(fList)

db = pymysql.connect("localhost","testuser","test123","TESTDB")
