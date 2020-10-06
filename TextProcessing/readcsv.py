import csv
fp = open('data.csv','r')
reader = csv.reader(fp)
for rec in reader:
    print(rec[0],rec[1],rec[2],rec[3])

fp.close()