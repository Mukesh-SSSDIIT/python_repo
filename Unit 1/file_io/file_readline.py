# fp = open("myfile1.txt","r")
# txt = fp.read(14)
# print(txt)
# fp.close()

# fp = open("myfile1.txt","r")
# while(1):
#     txt = fp.readline()
#     if txt == '':
#         break
#     print(txt)
# fp.close()

fp = open("myfile1.txt","r")
for line in fp:
    print(line)
fp.close()