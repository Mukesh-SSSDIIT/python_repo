import mysql.connector as con
from mysql.connector.cursor import MySQLCursorBuffered

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

student_id = input("Enter Student ID to delete : ")

mycursor = mydb.cursor()
args = (student_id,)
mycursor.execute("delete from student where student_id = %s",args)


if mycursor.rowcount == 0:
    print("No records deleted")
else:
    print(mycursor.rowcount, "record(s) Deleted successfully")