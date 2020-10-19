import mysql.connector as con
from mysql.connector.cursor import MySQLCursorBuffered

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

mycursor = mydb.cursor()
args = [
        ("Rugved","Ahmedabad","India"),
        ("Yajurved","Ahmedabad","India"),
        ("Arthavved","Ahmedabad","India"),
        ("Samved","Ahmedabad","India")
        ]

mycursor.executemany("insert into student(student_name,student_city,student_country) values(%s,%s,%s)",args)

print(mycursor.rowcount, "record(s) inserted successfully")
print("Last inserted record id :",mycursor.lastrowid)