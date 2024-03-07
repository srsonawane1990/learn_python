x = 10
print(x)

results = x > 100
print(results)

a = 10 
b = 20
print(x > b) #10 >10 = False
print (b > a) # True
print(x>=a) # True
print(a != b) #True


print(x > a and x > b ) #False and False ---> False
print (b > a and a == x ) # True and False ---> True
print(x>=a and a > b) # True and False ---> False
print(x>b and a != b) # False and True --- > False


print(x > a or x > b ) #False and False ---> False
print (b > a or a == x ) # True and False ---> True
print(x>=a or a > b) # True and False ---> True
print(x>b or a != b) # False and True --- > True

# bitwise operator
print(10 & 5)
print(10 & 8)

print(10 | 5)  #15
print(10 | 8)  #10
print(9<<2) #36
print(9<<1) #18
print(9>>2) #2
print(9>>1) #4
