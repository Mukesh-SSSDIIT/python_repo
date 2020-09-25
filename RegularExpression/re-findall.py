import re
m = re.findall("H.","Hi foo, How are you, How about you");
print(m)

s = "BCA6001-Mr. A,BSCIT6001-Mr.B,BCA6002-Mr.C"
re.findall('BCA6[0-9]{3}',s)

txt = "The rain in Spain ainstain"
x = re.findall(r"ain\B", txt)
print(x)

txt = "The rain in Spain ainstain"
x = re.findall(r"ain\b", txt)
print(x)

txt = "The rain in Spain at 09:30am"
x = re.findall("\d{2}", txt)
print(x)

txt = "The rain in Spain at 09:30am"
x = re.findall("\D", txt)
print(x)

txt = "The rain in Spain at 09:30am, how are you"
x = re.findall("\s", txt)
print(x)
print("Total words are",len(x)+1)

txt = "The rain in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("\w", txt)
print(x)

txt = "The rain in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("\W", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("you\Z", txt)
print(x)

# Sets

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[ypo]", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[a-m]", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[^ypo]", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[^a-m]", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[0123]", txt)
print(x)

txt = "The rain you in Sp_ain @ 09:30am,# ^ how are you"
x = re.findall("[0-9]", txt)
print(x)