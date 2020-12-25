import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor();
mycursor.execute("Create database pythonmysql1")
print("Database created successfully")