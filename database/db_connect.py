import pymysql
def sqlconnector():


  f=open(r"data1.csv","r")
  fstring = f.read()

  fList=[]
  for line in fstring.split('\n'):
    fList.append(line.split(','))
  print(fList)
  #CONNECT
  db = pymysql.connect("localhost","testuser","test123","TESTDB")
  cursor = db.cursor()
  # execute SQL query using execute() method.
  cursor.execute("SELECT VERSION()")

  # Fetch a single row using fetchone() method.
  data = cursor.fetchone()
  print ("Database version : %s " % data)
  # CREATE table as per requirement
  cursor.execute("DROP TABLE IF EXISTS JIVELY")
  sql = """CREATE TABLE JIVELY (
   NAME  CHAR(20) NOT NULL,
   HUMIDITY INT,  
   TEMPERATURE FLOAT)"""

  cursor.execute(sql)
  db.close()