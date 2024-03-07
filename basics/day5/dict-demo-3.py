ls = [
    {'name' : "John", "age" : "25", 'city' : 'Pune'},
    {'name' : "Bob", "age" : "26", 'city' : 'Mumbai'},
    {'name' : "Tina", "age" : "25", 'city' : 'Nasik'}
]

for rec in ls:
    for k,v in rec.items():
        print(k,v)
        print("------------")