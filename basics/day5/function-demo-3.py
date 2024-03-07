# Write a function to find the largest no if a and b are mandetory and c is an optional
def largest_of_3_nos(a,b,c=0):  # all mandentory elements first and optional in last
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(largest_of_3_nos(11,22,33))
print(largest_of_3_nos(44,55))