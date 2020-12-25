def linearsearch(list,searchvalue):
    position = 1
    for i in list:
        if i == searchvalue:
            return position
        else:
            position += 1
    return -1

lst = [10,4,2,90,5,58,60,57,42,3]
result = linearsearch(lst,57)
if result == -1:
    print("Search not found")
else:
    print("Search found on position",result)