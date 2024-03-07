fh = open('./sample.txt')
#print(fh.read())
for line in fh:
    print(line)
fh.close()