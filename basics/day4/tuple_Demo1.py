# tuple is similar to list only difference is 
# list is mutable where tuple is imutable (non modifiable/constant)
tp = (11, 22,33,44,55,66)
print(tp)
print(tp[0])
print(tp[-2])
#tp.append(10) # error AttributeError: 'tuple' object has no attribute 'append'
#tp[0] = 100 error: TypeError: 'tuple' object does not support item assignment
print(tp[0:2])
print(type(tp))
