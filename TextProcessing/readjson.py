# Python program to read JSON from a file.
import json 

# Opening JSON file 
with open('sample.json', 'r') as openfile: 

	# Reading from json file 
	json_object = json.load(openfile) 

print(json_object) 
print(type(json_object))