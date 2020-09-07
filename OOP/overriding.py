class A:
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname
    
    def printname(self):
        print(self.fname,self.lname)

class B(A):
    def __init__(self,firstname,middlename,lastname):
        self.middlename = middlename
        super().__init__(firstname,lastname)
    
    def printname(self):
        # super().printname();
        print(self.fname,self.middlename,self.lname)
    

b = B("Ram","Laxmanbhai","Desai")
b.printname()