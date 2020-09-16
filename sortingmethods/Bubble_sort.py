def bubblesort(list):
    l = len(list)
    for i in range(0,l-1):
        for j in range(l-1,i,-1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list            


lst = [5,200,-20,16,-11]
result = bubblesort(lst)
print(result)
