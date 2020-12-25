# Will create a file if it does not exists
# If file exist, will raise error.
fp = open('myfile3.txt',"x")
fp.write("Good Morning\n")
fp.close()

fp = open("myfile3.txt","r")
print(fp.read())
fp.close()