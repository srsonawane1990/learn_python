d1 = {'name' : "Bob", 'age' : '25', 'City': 'Pune'}
print(d1.keys())

for key in d1.keys():
    print("Key - ", key, ' Value - ', d1[key])

print("-----------------------------------------")

print(d1.values())
for Val in d1.values():
    print(Val)

print("-----------------------------------------")

print(d1.items())
for k,v in d1.items():
    print(k,v)
print("-----------------------------------------")
#access data using get function

for k in d1.keys():
    print(d1.get(k))  # d1.get(k) is similar to d1[k]

