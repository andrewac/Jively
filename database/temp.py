'''
import random
f=open("newfile.txt","w")
for x in range(10):
    line=str(random.randint(1,100))
    f.write(line)
    f.write(",")
    
    
'''

''' 
import csv
import random
listoflists = []
a_list = []
b_list=[]
c_list=[]
import pandas 
import sqlalchemy
import pyodbc
#engine = create_engine('mssql+pyodbc://username:password@mydsn')

inside=[]
for i in range(0,10):
    a_list.append(str(random.randint(1,100)))
for j in range(0,10):
    b_list.append(str(random.randint(0,60)))
    #if len(a_list)>2:
        #a_list.remove(a_list[0])
        #listoflists.append((list(a_list)))
#print(listoflists)
print(a_list)
print(b_list)
for k in range(0,10):
    inside=[a_list[k],b_list[k]]
    c_list.append(inside)
    
print(c_list)
#data = [['column1','column2'],['data11','data12'],['data21','data22']]
csv_file = open(r'data1.csv', 'w')
with csv_file:
   writer = csv.writer(csv_file)
   writer.writerow(['Humidity','Temperature'])   
   writer.writerows(c_list)
   print("Done")

# read csv data to dataframe with pandas
# datatypes will be assumed
# pandas is smart but you can specify datatypes with the `dtype` parameter
#df = pandas.read_csv('data1.csv')

# write to sql table... pandas will use default column names and dtypes
#df.to_sql('table_name',engine,index=True,index_label='id')

# add 'dtype' parameter to specify datatypes if needed; 
#dtype={'column1':VARCHAR(255), 'column2':DateTime}
'''
import pymysql
f=open(r"data1.csv","r")
fstring = f.read()

fList=[]
for line in fstring.split('\n'):
    fList.append(line.split(','))
print(fList)

db = pymysql.connect("localhost","testuser","test123","TESTDB")
'''
Generates random numbers for the temperature and humidity sensor
Humidity in percentages
'''
