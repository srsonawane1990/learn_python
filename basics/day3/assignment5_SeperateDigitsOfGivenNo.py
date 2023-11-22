# Separate digits of given numbers
# 1234 ===> 1,2,3,4

number = int(input("Enter no : "))
string = str(number)
list_of_digits = []
for i in string:
    list_of_digits.append(int(i))
print(list_of_digits)

#int_num = int(input("Enter no : "))
#empty = []
#while int_num > 0:
#    int_num, remd = divmod(int_num, 10)
#    empty.append(remd) 
#print(empty)
