# Find the largest of 10 numbers. Given as inputs by user
i = 1
max = int(input("Enter the value : "))
while i < 10:
    new_val = int(input("Enter the value: "))
    if new_val > max:
        max = new_val
    i += 1
print(max) 
