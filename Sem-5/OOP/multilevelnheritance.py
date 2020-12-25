class A:
    classAVariable = 5

class B(A): # Multilevel inheritance
    classBVariable = 6

class C(B): # Multilevel inheritance
    classCVariable = 7

c = C()
print(c.classAVariable)
print(c.classBVariable)
print(c.classCVariable)