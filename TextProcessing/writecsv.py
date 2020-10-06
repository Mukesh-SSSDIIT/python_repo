import csv

data = (
    (6,'bbb','Rjt',321456),
    (7,'bab','Jnd',323456),
    (8,'bac','Abd',324456),
)

fp = open("data.csv","a")
writer = csv.writer(fp)
for row in data:
    writer.writerow(row)

fp.close()