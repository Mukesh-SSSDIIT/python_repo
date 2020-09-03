# Will create a file if it does not exists
# If file exist, content will be appended.
fp = open('myfile2.txt',"a")
fp.write("Good Morning\n")
fp.close()

fp = open("myfile2.txt","r")
print(fp.read())
fp.close()