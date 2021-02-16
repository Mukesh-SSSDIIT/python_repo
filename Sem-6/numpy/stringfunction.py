import numpy as np   
# print("Concatenating two string arrays:")  
# print(np.char.add(['welcome','Hi'], [' to Javatpoint', ' read python'] ))  

# print("Printing a string multiple times:")  
# print(np.char.multiply("hello ",3))  

# print(np.char.center("SSSDIIT", 50, '*'))  

# print(np.char.capitalize("welcome to javatpoint"))  

# print(np.char.title("welcome to javatpoint"))  

# print(np.char.lower("WELCOME TO JAVATPOINT"))  

# print(np.char.upper("Welcome To Javatpoint"))  

# print(np.char.split("Wel-come To Javatpoint"),sep="-")  

# print(np.char.splitlines("Welcome\nTo\nJavatpoint"))

# str = "     welcome to javatpoint     "  
# print("Original String:",str)  
# print("Removing the leading and trailing whitespaces from the string")  
# print(np.char.strip(str))  

# print(np.char.join('---','ABCDEFGHIJK'))  

# str = "Welcome to Javatpoint"  
# print("Original String:",str)  
# print("Modified String:",end=" ")  
# print(np.char.replace(str, "Welcome to","www."))

enstr = np.char.encode("welcome to javatpoint", 'cp500')  
dstr =np.char.decode(enstr, 'cp500')  
print(enstr)  
print(dstr)  