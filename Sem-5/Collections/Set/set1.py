# Declaring Set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
print(set1)

# Iterate through Set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}

for item in set1:
    print(item)

# Add item to set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.add("NewFruit")
for item in set1:
    print(item)

# Add multiple items in a set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.update(['Item1','Item2','Item3'])
for item in set1:
    print(item)

# Length of set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
print(len(set1))

# Remove item using remove method
# If the item to remove does not exist, remove() will raise an error. 
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.remove("Banana")
print(set1)

# Remove item item using discard method
# If the item to remove does not exist, discard() will NOT raise an error.
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.discard("Bananas")
print(set1)

# Remove item using pop method
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.pop()
print(set1)

# Clear all items from set using clear()
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
set1.clear()
print(set1)

# Delete set
set1 = {"Apple","Banana","Cherry","Mango","Pinapple"}
del set1
print(set1)

# Merge sets using union method
# Both union() and update() will exclude any duplicate items
set1 = {"Apple","Banana","Cherry","Mango"}
set2 = {"Mango","Pinapple"}
set3 = set1.union(set2)
print(set1)
print(set2)
print(set3)

# Merge sets using update method
# Both union() and update() will exclude any duplicate items
set1 = {"Apple","Banana","Cherry","Mango"}
set2 = {"Mango","Pinapple"}
set1.update(set2)
print(set1)
print(set2)

# Declaring set using set constructor
set1 = set(('Banana','Mango'))
print(set1)
print(type(set1))

# Copy one set into another set
set1 = set(('Banana','Mango'))
set2 = set1.copy()
set2.add("apple")
set1.add("aaa")
print(set1)
print(set2)