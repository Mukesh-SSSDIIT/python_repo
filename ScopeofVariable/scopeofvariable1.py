a = 10 # global
s = 1 # global

def myfunction():
    def myfunction1():
        global a
        global s
        a = 5
        s = a * a
        print(a,s)
    print(a,s) # 10, 1
    myfunction1(); # 5,25
    print(a,s) # 5, 1

myfunction()