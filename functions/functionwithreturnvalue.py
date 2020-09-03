def sqaure(a):
    s = a * a
    q = a * a * a
    return a,s,q

a = sqaure(4)
print(a[0])
print(a[1])
print(a[2])

b,c,d = sqaure(5)
print(b,c,d)

# e,f = sqaure(6) ## Will raise error
# print(e,f)

