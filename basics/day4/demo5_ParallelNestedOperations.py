a = [1, 2, 3]
b = [7, 8, 9]
d = [(x + y) for (x,y) in zip(a,b)]  # parallel iterators
# output => [8, 10, 12]
e = [(x,y) for x in a for y in b]    # nested iterators
# output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)] 
print(d)
print(e)
