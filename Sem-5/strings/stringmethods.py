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
txt = "My name is {fname}, I'm {age} year old."
txt1 = txt.format(fname = "Aakash", age = 36)
txt2 = txt.format(fname = "Shiv", age = 42)
txt3 = txt.format(fname = "Aman", age = 48)
print(txt)
print(txt1)
print(txt2)
print(txt3)

#numbered indexes:
txt = "My name is {0}, I'm {1} year old. Hi {0}, you are {1} year old"
txt1 = txt.format("Aakash",36)
print(txt1)

#empty placeholder:
txt = "My name is {}, I'm {} year old. Hi {}"
txt1 = txt.format("Aakash",36, "Shiv")
print(txt1)

#Inside the placeholders you can add a formatting type to format the result:
# :<	Left aligns the result (within the available space)
# :>	Right aligns the result (within the available space)
# :^	Center aligns the result (within the available space)
# :=	Places the sign to the left most position
# :+	Use a plus sign to indicate if the result is positive or negative
# : 	Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
# :,	Use a comma as a thousand separator
# :_	Use a underscore as a thousand separator
# :b	Binary format
# :c	Converts the value into the corresponding unicode character (ASCII Value)
# :d	Decimal format
# :e	Scientific format, with a lower case e
# :E	Scientific format, with a lower case E
# :f	Fix point number format
# :o	Octal format
# :x	Hex format, lower case
# :X	Hex format, upper case
# :n	Number format
# :%	Percentage format

txt = "i love {:^15} India is my country"
print(txt.format("India"))


# index() - Searches the string for a specified value and returns the position of where it was found
# if string is not found in the main string then this method will raise an error.

txt = "Hello, welcome to my world."
x = txt.index("to")
print(x)

# isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Compa4&52AAaaany12"
x = txt.isalnum()
print(x)

# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "Company"
x = txt.isalpha()
print(x)

# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
txt = "\u0039"
print(txt)
x = txt.isdecimal()
print(x)

# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
txt = "12\u00B3"
print(txt)
x = txt.isdigit()
print(x)

# The isidentifier() method returns True if the string is a valid identifier, 
# otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) 
# and (0-9), or underscores (_). A valid identifier cannot start with a number, 
# or contain any spaces.
txt = "ABC_123"
x = txt.isidentifier()
print(x)

# The islower() method returns True if all the characters are in lower case, 
# otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "abc_123"
x = txt.islower()
print(x)

# The isupper() method returns True if all the characters are in upper case, 
# otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "ABC_123"
x = txt.isupper()
print(x)

# The istitle() method returns True if all words in a text start with a 
# upper case letter, AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.
txt = "Hello Friends How Are You"
x = txt.istitle()
print(x)

# The isnumeric() method returns True if all the characters are numeric (0-9), 
# otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
txt = "1234"
x = txt.isnumeric()
print(x)

# The isprintable() method returns True if all the characters are printable, 
# otherwise False.
# Example of none printable character can be carriage return and line feed.
txt = "ABC\t1234"
print(txt)
x = txt.isprintable()
print(x)

# The isspace() method returns True if all the characters in a string are whitespaces, 
# otherwise False.
txt = "   "
x = txt.isspace()
print(x)

# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
myValues= ["John", "Peter", "Vicky"]
myseparator = "-"
x = myseparator.join(myValues)
print(x)

myValues= ["John", "Peter", "Vicky"]
x = "-".join(myValues)
print(x)

# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# lower()	Converts a string into lower case
txt = "APPle"
x = txt.lower()
print(x)

# The lstrip() method removes any leading characters (space is the default leading character to remove)
txt = "------banana     "
x = txt.lstrip('-')
print("of all fruits", x, "is my favorite")

# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
txt = "       banana------"
x = txt.rstrip('-')
print("of all fruits", x, "is my favorite")

# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "-------banana------"
x = txt.strip("-")
print("of all fruits", x, "is my favorite")

# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
txt = "Hello Sam!"
mytable = txt.maketrans("HmSa", "CeJo",'l')
print(txt.translate(mytable))

# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "Rajesh-Shiv"
x = txt.partition("-")
print(x)

# The replace() method replaces a specified phrase with another specified phrase.
# All occurrences of the specified phrase will be replaced, if nothing else is specified.
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three",2)
print(x)

# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method.

txt = "Mi casa, su casa."
x = txt.rfind("casa",0,10)
print(x)

# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(20)
print("Hello, ",x, "is my favorite fruit.")

# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# The rsplit() method splits a string into a list, starting from the right.
# If no "max" is specified, this method will return the same as the split() method.
txt = "apple, banana, cherry"
x = txt.rsplit(", ",1)
print(x)

# The splitlines() method splits a string into a list. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to\nthe jungle"
x = txt.splitlines()
print(x)

# The startswith() method returns True if the string starts with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.startswith("welcome")
print(x)

# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
txt = "512"
x = txt.zfill(5)
print(x)