# Factorial n
# n! = 1 * 2 * 3 * 4 * ...... * n

i = 1
x = 1
no = int(input("Enter no : "))
while i <= no:
    x = i * x
    i += 1
print("Factorial of given no is : ", x)
