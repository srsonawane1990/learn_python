# write a function to find factorial n!
def fact(n):
    a = 1
    fact = 1
    while a <= n:
        fact = fact * a
        a +=1
    print(f"factoriable of {n} is {fact}.") 
fact(5)
fact(4)
fact(3)
fact(2)
