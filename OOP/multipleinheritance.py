class A:
    classAVariable = 5

class B:
    classBVariable = 6

class C(A,B): # Multiple inheritance
    classCVariable = 7

c = C()
print(c.classAVariable)
print(c.classBVariable)
print(c.classCVariable)