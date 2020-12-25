def selectionsort(list):
    l = len(list)
    for i in range(0,l):
        minindex = i
        for j in range(i+1,l):
            if(list[minindex] > list[j]):
                minindex = j
        if(i != minindex):
            list[i] , list[minindex] = list[minindex],list[i]
    return list

lst =[-40,8,-69,4,56]
result = selectionsort(lst)
print(result)