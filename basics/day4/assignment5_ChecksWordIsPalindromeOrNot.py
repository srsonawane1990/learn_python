# Check the word is it palindrome or not 
# palindrome means reverse string is similar to given string

word = input("Enter the word : ")
if word == word[::-1]:
    print("The list is palindrome")
else:
    print("The list is not palindrome")

