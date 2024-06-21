# Fetch the all the values in list using negating index using while loop

ls = [11,22,33]
print(ls[0],ls[-2])
i = -1
n = -len(ls)

print(ls[::-1])

while i >= n:
    print(ls[n])
    n += 1

for i in ls:
    print(i)
