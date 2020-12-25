class A:
    classAVariable = 5

class B(A): # Hierarchical inheritance
    classBVariable = 6

class C(A): # Hierarchical inheritance
    classCVariable = 7

class D(A): # Hierarchical inheritance
    classDVariable = 8

b = B()
print(b.classAVariable)
print(b.classBVariable)

c = C()
print(c.classAVariable)
print(c.classCVariable)

d = D()
print(d.classAVariable)
print(d.classDVariable)