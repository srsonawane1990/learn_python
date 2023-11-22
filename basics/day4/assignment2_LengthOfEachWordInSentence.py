# Write a program to find the length of each word in a sentence ( take sentance as input from user )

str = input("Enter senternce : ")

words = str.split()

for length in words:
    print("The length of the word '{}' is {}".format(length,len(length)))

