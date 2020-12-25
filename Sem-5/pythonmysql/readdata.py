import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

mycursor = mydb.cursor()
mycursor.execute("select * from student")

firststudent = mycursor.fetchone();
print(firststudent)

students = mycursor.fetchall()


print("List of students")
print("No\t Name\t City")
print("------------------------")
for student in students:
    print(student[0],"\t",student[1],"\t",student[2])