# slicing of listing
ls = [11,22,33,44,55,66]
print(ls[0:2]) # [start_index : end_index] where end index is not inclusive
print(ls[2:])
print(ls[:3])
print(ls[:])
print(ls[0:-2])
print(ls[-6:-3])
a,b,c = ls[0:3] #unpacking i = 0 ----> i < 3
print(a,b,c)
