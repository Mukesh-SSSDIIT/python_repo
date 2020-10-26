import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

mycursor = mydb.cursor()
sql = "select s.student_name,s.student_city,b.book_id, b.tran_id from student as s left JOIN bookissue as b on s.student_id = b.student_id"
mycursor.execute(sql)

students = mycursor.fetchall()

for student in students:
    print(student)





