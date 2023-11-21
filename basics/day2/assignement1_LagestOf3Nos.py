# Largest of 3 nos (using and operator)

n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))

if (n1 > n2 and n1 > n3):
    print(n1, " is the largest no")
elif n2 > n3:
    print(n2, " is the largest ")
else: 
    print(n3, " is the largest ")
