import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

mydb.autocommit =False 

mycursor = mydb.cursor()

args = ('bbb',1)
mycursor.execute("update student set student_name = %s where student_id = %s",args)

args = ('bbbbbb',2)
mycursor.execute("update student set student_name = %s where student_id = %s",args)

mydb.rollback()

print(mycursor.rowcount, "record(s) updated successfully")

mycursor.close()
mydb.close()