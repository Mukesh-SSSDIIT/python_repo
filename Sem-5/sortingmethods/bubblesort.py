mylist = [10,5,6,1,100,88,99,40,51,70]
# for i in range(10):
#     v = int(input("Enter number : "))
#     mylist.append(v)
l = len(mylist)
for i in range(0,l-1):
    for j in range(l-1,i,-1):
        if(mylist[j] < mylist[j-1]):
            mylist[j],mylist[j-1] = mylist[j-1],mylist[j]

print(mylist)