class A:
    classAVariable = 5

class B(A): # Single Inheritance.
    classBVariable = 6

b = B()
print(b.classAVariable)
print(b.classBVariable)