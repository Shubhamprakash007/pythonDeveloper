import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shubham123",
  database="mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#if table already exits 
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")