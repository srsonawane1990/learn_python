# Write a program to create a list which will store the length of each word of a sentence
# eg. This is test == [4,2,4]

sentence = input("Enter sentence : ")
words = sentence.split()
ls_length = []
ls_words = []

for word in words:
    out_length = ls_length.append(len(word))

print("{} : {}".format(sentence,ls_length))
