# Declare Dictionary
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19
    }
print(student)

# Access dictionary items by its key.
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19
    }
print(student["name"])
print(student["class"])
print(student["age"])

# Change value of dictionary item
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19
    }

student['name'] = "Bunty"
print(student['name'])

# Loop through dictionary
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

for k in student:
    print(k, " - ", student[k])

# values() - to get all values of dictionary
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

for v in student.values():
    print(v)

# items() - to access all keys and values
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

for k,v in student.items():
    print(k, "-" ,v)

# 'in' Operator to verify, whether key is available in dictionary or not.
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

if "age" in student:
    print("Age available : ",student['age'])
else:
    print("Age not available")

# len()
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

print(len(student))

# Add item
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }
student["semester"] = "5th Sem"
for k,v in student.items():
    print(k,v)

# Remove Item
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }
student.pop("class") # Specified item will be removed.
student.popitem() # Last item will be removed.
for k,v in student.items():
    print(k,v)

# clear()
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }
student.clear()
print(student)

# del keyword
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }
del student['class']
print(student)

# del keyword - To delete dictionary
student = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }
del student
print(student)

# Copy dictionary
student1 = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

student2 = student1.copy()
student1['name'] = "Ramesh"
student2['name'] = "Jayesh"
print(student1)
print(student2)

# Copy dictionary using dict()
student1 = {
    "name":"Rakesh",
    "class":"bca",
    "age":19,
    "percentage":89
    }

student2 = dict(student1)
student1['name'] = "Ramesh"
student2['name'] = "Jayesh"
print(student1)
print(student2)

# Nested Dictionary
myfamily = {
    "child1": {
        'name':"Mr.A",
        'Age':19
    },
    "child2":{
        'name':"Mr.B",
        'Age':20
    },
    "child3":{
        'name':"Mr.C",
        'Age':25
    }
}
print(myfamily)
for k,v in myfamily.items():
    #print(k,v)
    print(k)
    #print(v["name"])
    #print(v["Age"])
    for ck,cv in v.items():
        print(ck,cv)