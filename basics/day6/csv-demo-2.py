import csv
fh = open('./Day7/emp.csv')
reader = csv.reader(fh)
next(reader)
for rec in reader:
    print(rec)
fh.close()