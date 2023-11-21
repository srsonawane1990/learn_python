n1 = int(input("Enter the 1st value : "))
n2 = int(input("Enter the 2nd value : "))
n3 = int(input("Enter the 3rd value : "))

if n1 > n2:
    if n1 > n3:
        print(n1, " Largest")
    else:
        print(n3, " Largest")
else:
    if n2 > n3:
        print(n2, " Largest")
    else:
        print(n3, " Largest")

