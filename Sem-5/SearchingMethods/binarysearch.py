def binarysearch(list,searchvalue):
    l = 0
    h = len(list) - 1
    while l <= h:
        m = int((l + h) / 2)
        if list[m] == searchvalue:
            return m;
        elif list[m] < searchvalue:
            l = m + 1
        elif list[m] > searchvalue:
            h = m - 1
    return -1

rollno = [2, 3, 6, 11, 12, 44, 55, 69, 83, 87]
# The list must be in sorted order
rollno.sort()
print(rollno)
result = binarysearch(rollno,87)
if result == -1:
    print("Search not found")
else:
    print("Search found on position",result+1)