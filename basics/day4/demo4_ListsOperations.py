my_list = [2, 4, 1, 3, 5, 10, 22, 7, 11]
squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]
print(squared_list)
squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
print(squared_dict)

my_list = [2, 4, 1, 3, 5, 10, 22, 7, 11]
squared_list = [x**2 for x in my_list if x%2 != 0]    # list comprehension
# output => [9 , 25 , 49 , 121]
print(squared_list)
squared_dict = {x:x**2 for x in my_list if x%2 != 0}    # dict comprehension
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}
print(squared_dict)

x = []

for i in my_list:
    if i%2 == 0:
        x.append(i)
for i in my_list:
    if i%2 != 0:
        x.append(i)
print(x)