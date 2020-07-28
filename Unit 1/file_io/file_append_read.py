import os

fp = open("myfile2.txt","a+")
fp.write("this is new content\n")
# fp.close()
# fp = open("myfile1.txt","r")

# The tell method of the filehandle will return the current location of this pointer.
print(fp.tell())
fp.seek(4,os.SEEK_SET)
print(fp.tell())
# os.SEEK_SET - Begining of the file
# os.SEEK_CUR - current position
# os.SEEK_END - end of file

txt = fp.read(6)
print(txt)
filesize = os.path.getsize("myfile2.txt")
totallines = filesize/21
print(totallines)
fp.seek(5*21,os.SEEK_SET)
print(fp.read(1))
fp.close()