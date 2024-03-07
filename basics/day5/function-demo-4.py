print("Hi")
print("Hi","Hello")
print("Hi","Hello","Welcome")
print("Hi","Hello", "Welcome", "Saama")

# Write function which will add n numbers

def add_numbers(*var_params):   # var_params is of type TUPLE (*var_params will take any numbers of inputs)
    total = 0
    for val in var_params:
        total += val
    return total
print(add_numbers(1,2,3)) # var_params = (1,2,3)
print(add_numbers(1,2,3,11,22,33)) # var_params = (1,2,3,11,22,33)
print(add_numbers(1,2,3,11,22,33,55,333,4555)) # var_params = (1,2,3,11,22,33,55,333,4555)
