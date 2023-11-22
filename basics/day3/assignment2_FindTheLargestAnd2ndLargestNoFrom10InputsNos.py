# Find Largest and 2nd largest valye from 10 inputs given user. (even if incase of negative number)
max = int(input("Enter value : "))
n = int(input("Enter value : "))
i = 1

if max < n:
    second_max = max
    max  = n
else:
    second_max = n

while i < 9:
    n = int(input("Enter value : "))
    if max < n:
        second_max = max
        max  = n
    elif second_max < n:
        second_max = n
    i += 1
print(max)
print(second_max)
