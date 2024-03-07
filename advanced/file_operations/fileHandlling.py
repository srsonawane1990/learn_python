import os
# create a file

os.remove("sample.txt")
file = open("sample.txt", 'x')


# write to a file
file = open("test.txt", "w")
file.write("This is an example of file creation")
file.close

# read a file
file = open("test.txt", 'r')
print(file.read())
file.close

# Append a file
file = open("test.txt", 'a')
file.write("This is an example of append a file")
# print(file.read())         # It will give the error because it (file) not readable 
file.close

#os.remove("test.txt")
