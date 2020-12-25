class Student: # Class Defination
    def __init__(self,rno,name): # constructor
        self.rollno = 5
        self.nameofstudent = name

    def showname(self):
        print(self.nameofstudent)
    
    def test(self):
        print("abc")

class test:
    pass

s1 = Student(5,"Ram"); # Creating Object
s1.showname()
s1.nameofstudent ="Shyam"
#del s1.nameofstudent
s1.showname()
s1.test()
# del s1
# s1.showname()