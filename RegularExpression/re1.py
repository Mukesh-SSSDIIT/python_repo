import re
m = re.search("Hodw","Hi foo, How are you");
if m == None:
    print("Search not found")
else:
    print("Search found")
    print(m)