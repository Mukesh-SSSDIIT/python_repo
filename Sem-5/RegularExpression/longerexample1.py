import re

fp = open("longerexample.txt","r")
txt = fp.read()

result = re.findall('(Mon|Tue|Web|Thu|Fri|Sat|Sun)',txt)
print(result)

result = re.findall('\d+-\d+-\d+',txt)
print(result)

result = re.findall('[0-9]+-[0-9]+-[0-9]+',txt)
print(result)

result = re.findall('[0-9]{3}',txt)
print(result)

