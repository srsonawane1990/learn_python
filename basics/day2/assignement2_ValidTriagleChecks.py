# problem 1: Read length of 3 sides, and check will it form a valid triangle
# (sum of two sides must be greater than 3rd side)
# problem 2: If length of 3 sides are given, find which type of triangle.
# problem 3: combination prob 1 and prob 2 as one solution

side1 = int(input("Please enter the 1st side of the length "))
side2 = int(input("Please enter the 2nd side of the length "))
side3 = int(input("Please enter the 3rd side of the length "))

if (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2:
    print("It forms a valid triangle!!")
    if side1 == side2 == side3:
        print("The triagle is Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triagle is isosceles triagles")
    elif side1 != side2 or side2 != side3 or side1 != side3:
        print("The triangle is scalene triangle")
else:
    print("It doesn't form a valid triangle!!")

