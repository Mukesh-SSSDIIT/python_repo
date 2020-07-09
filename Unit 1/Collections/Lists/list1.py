fruits = ["Apple","Bananas","Pineapple","Cherry","kiwi","mango","melon"]

print(fruits)

print("\nAccess individual item from list")
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("\nAccess list using loop")
for fruit in fruits:
    print(fruit)

print("\nAccess list using loop")
for i in range(len(fruits)):
    print(fruits[i])

print("\nNegative Indexing")
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

print("\nAccess list using loop - Negative Indexing")
length = len(fruits) + 1
length = -length
for i in range(-1,length,-1):
    print(fruits[i])

print("\nRange of index")
newfruitlist = fruits[1:6]
print(newfruitlist)
print(newfruitlist[0])

if "Banana" in fruits:
    print("'\nBanana is in the list")
else:
    print("\nBanana is not in the list")


