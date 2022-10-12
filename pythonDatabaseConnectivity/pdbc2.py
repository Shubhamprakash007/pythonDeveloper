import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shubham123"
)

print(mydb)