import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'python_example_db'
)

username = input("Username : ")
password = input("Password : ")

mycursor = mydb.cursor()

sql = "select * from users where username = '"+username+"' and password = '" + password + "'"
print(sql)
mycursor.execute(sql,multi=True)
user =  mycursor.fetchone()
print(user)
if user is None:
    print("Not a valid username or password")
else:
    print("Welcome to the Python program")