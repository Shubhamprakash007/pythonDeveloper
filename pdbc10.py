import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shubham123",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)