# Will create a file if it does not exists
# If file exist, it will be overwritten.
fp = open('myfile1.txt',"w")
fp.write("Good Morning")
fp.close()

fp = open("myfile1.txt","r")
print(fp.read())
fp.close
