# Declaring Tuple
fruit_tuple = ("Apple","Banana","Mango")
print(fruit_tuple)

# Access Tuple Items
print(fruit_tuple[0])

# Iterate through Tuple
for t in fruit_tuple:
    print (t)

# Iterate tuple through index number
length = len(fruit_tuple)
for i in range(length):
    print(fruit_tuple[i])

# Change the tuple values indirectly.
fruit_tuple = ("Apple","Banana","Mango")
fruit_list = list(fruit_tuple)
fruit_list[1] = "Cherry"
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

# Delete entire tuple
fruit_tuple = ("Apple","Banana","Mango")
del fruit_tuple