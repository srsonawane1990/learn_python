# Count the number of words in a file

file = open("test.txt", "r")
content = file.read()
print(content)
words = content.split()
count = 0
print(len(words))
print(words)
for i in words:
    count += 1
print(count)
