# Python program to write JSON to a file.

import json 

# Data to be written 
dictionary ={ 
	"name" : "sathiyajith", 
	"rollno" : 56, 
	"cgpa" : 8.6, 
	"phonenumber" : "9999900000"
} 

# Serializing json 
json_object = json.dumps(dictionary, indent = 4) 

# Writing to sample.json 
with open("sample.json", "w") as outfile: 
	outfile.write(json_object)
