# The strip() method removes any whitespace from the beginning or the end
s1 = "    India is great     "
print("start:",s1.strip(),":end")

# The lower() method returns the string in lower case:
s1 = "India is great"
print(s1.lower())

# The upper() method returns the string in upper case:
s1 = "India is great"
print(s1.upper())

# The replace() method replaces a string with another string:
s1 = "India is great"
print(s1.replace("great","my country"))

# The split() method splits the string into substrings if it finds instances of the separator:
s1 = "Rakesh,Prakash,Mohit,Manas"
l1 = s1.split(",")
for s in l1:
    print(s)

# capitalize()	Converts the first character to upper case
s1 = "i loVe My India"
print(s1.capitalize())

# casefold()	Converts string into lower case
s1 = "I LoVe My India"
print(s1.casefold())

# center()	Returns a centered string
s1 = "India"
print(".",s1.center(20),".")

# count()	Returns the number of times a specified value occurs in a string
s1 = "I love india, India is my country"
print(s1.count('I'))

s1 = "I love india, India is my country"
print(s1.upper().count('I',13,18)) # character,start,end

# encode()	Returns an encoded version of the string
s1 = "What is yo◘r name"
print(s1.encode())

# endswith()	Returns true if the string ends with the specified value
s1 = "What is your name? My name is Rakesh."
print(s1.endswith("?"))

# The expandtabs() method sets the tab size to the specified number of whitespaces.
s1 = "i\tn\td\ti\ta"
print(s1.expandtabs(5))

# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

s1 = "India is great country in the world. great people leaves here"
print(s1.find("great",10,42))

# Another Example of find()
s1 = "India is great country in the world. great people leaves here"
searchstring = "great"
start = s1.find(searchstring,10,42)
end = start + len(searchstring)
print(start,end)
print(s1[start:end])

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.

#named indexes:
txt = "My name is {fname}, I'm {age}"
txt1 = txt.format(fname = "Aakash", age = 36)
txt2 = txt.format(fname = "Shiv", age = 42)
txt3 = txt.format(fname = "Aman", age = 48)
print(txt)
print(txt1)
print(txt2)
print(txt3)

