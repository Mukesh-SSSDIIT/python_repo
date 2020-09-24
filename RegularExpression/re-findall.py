import re
m = re.findall("H.","Hi foo, How are you, How about you");
print(m)

s = "BCA6001-Mr. A,BSCIT6001-Mr.B,BCA6002-Mr.C"
re.findall('BCA6[0-9]{3}',s)

