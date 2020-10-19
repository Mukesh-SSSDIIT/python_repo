import mysql.connector as con
from mysql.connector.cursor import MySQLCursorBuffered

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

student_id = input("Enter Student Id : ")
name = input("Name : ")
city = input("City : ")
country = input("Country : ")

mycursor = mydb.cursor()
args = (student_id,name,city,country)
mycursor.execute("insert into student values(%s,%s,%s,%s)",args)

print(mycursor.rowcount, "record(s) inserted successfully")
print("Last Record id : ",mycursor.lastrowid)