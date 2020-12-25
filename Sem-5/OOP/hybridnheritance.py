# Hybrid Inheritance
class A:
    classAVariable = 5

class B(A): # Hierarchical inheritance
    classBVariable = 6

class C(A): # Hierarchical inheritance
    classCVariable = 7

class D(B,C): # Multiple inheritance
    classDVariable = 8

d = D()
print(d.classAVariable)
print(d.classBVariable)
print(d.classCVariable)
print(d.classDVariable)