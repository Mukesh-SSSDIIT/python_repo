import re

fp = open("data.txt","r")
data = fp.read();
result = re.findall("\d{10}",data)
print(result)

result = re.findall("\d{2}[-|/]\d{2}[-|/]\d{4}",data)
print(result)

result = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-..]+",data)
print(result)




