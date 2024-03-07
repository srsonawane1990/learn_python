x = 10  # Global variable

def change():
    global x
    x = 10000   # Local variable
    y = 100

    print("Inside Function : ", x,y)

print("Inside Function : ", x)
change()
print("Outsde Function : ", x)
