import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shubham123",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)