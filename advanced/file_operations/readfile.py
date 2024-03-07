f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline()) #This reads only line one by one
f.close()
