fruits = ["Apple","Bananas","Pineapple"]
print(fruits)

# Add item at the end of the list
fruits.append("Cherry")
print(fruits)

# Insert method
fruits = ["Apple","Bananas","Pineapple"]
fruits.insert(2,"abcd")
print(fruits)

# Delete particular item
fruits.remove("Bananas")
print(fruits)

# Delete last item
fruits.pop()
print(fruits)

# Delete item from list
del fruits[1]
print(fruits)

# Delete entire list
del fruits
print(fruits) # Error becuase list is deleted.

# clear method
fruits = ["Apple","Bananas","Pineapple"]
fruits.clear()
print(fruits)
print(len(fruits))

# Copy a list
fruits1 = ["Apple","Bananas","Pineapple"]
fruits2 = fruits1.copy()
print(fruits1)
print(fruits2)
fruits2.pop()
print(fruits1)
print(fruits2)

# another way to copy list
fruits1 = ["Apple","Bananas","Pineapple"]
fruits2 = list(fruits1)
print(fruits1)
print(fruits2)
fruits2.pop()
print(fruits1)
print(fruits2)

# Join lists
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# Another way to join lists
list1 = ['a','b','c']
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1)

# Extend method to append items from another list
list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)

# Use list constructor
list1 = list((1,2,3,4,5))
print(list1)

