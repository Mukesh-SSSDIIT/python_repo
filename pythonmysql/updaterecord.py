import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

mycursor = mydb.cursor()
args = ('Ramesh',5)
mycursor.execute("update student set student_name = %s where student_id = %s",args)

print(mycursor.rowcount, "record(s) updated successfully")