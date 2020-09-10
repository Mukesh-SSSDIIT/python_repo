# Like other languages (for example method overloading in C++) do, 
# python does not supports method overloading by default. 
class Test: 

    def sum(self,a,b):
        return a + b
    
    def sum(self,a,b,c):
        return a + b + c

    def sum(self,a):
        return a;

test = Test()
ans = test.sum(5)
#ans = test.sum(5,10,20)
print(ans)

