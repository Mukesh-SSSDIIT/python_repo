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

# Declaring tuple with single item. Comma is required after first tiem.
mytuple = ("apple",)
print(type(mytuple))

# Joining tuples
tuple1 = ("a","b","c")
tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2
print(tuple3)

# Create tuple using constructor
tuple1 = tuple(("a","b","c"))
print(tuple1)

# Count Method
tuple1 = tuple(("a","b","c","a","b","a"))
print(tuple1.count("c"))

# Index Method
tuple1 = tuple(("a","b","c","a","b","a"))
print(tuple1.index("c"))