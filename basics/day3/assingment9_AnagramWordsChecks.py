# anagram words check
str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")
w1 = list(str1)
w2 = list(str2)

w1.sort()
print(w1)
w2.sort()
print(w2)

if w1 == w2:
    print("Matching words!!")
else:
    print("Not matching workds!!")
