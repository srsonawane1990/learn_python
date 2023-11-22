s1 = input("Enter string 1 ")
s2 = input("Enter string 2 ")

if s2.lower() in s1.lower():
    print("{} is present in: {} ".format(s2,s1))
else:
    print("{} is not present in: {} ".format(s2,s1))
