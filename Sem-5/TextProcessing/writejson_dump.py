# Python program to write JSON to a file 

import json 

# Data to be written 
dictionary ={ 
	"name" : "sathiyajith", 
	"rollno" : 56, 
	"cgpa" : 8.6, 
	"phonenumber" : "9999900000"
} 

with open("sample1.json", "w") as outfile: 
	json.dump(dictionary, outfile) 
