# count digits, alphabets and special chars in string

ip = "swapni sonawane 213431 *&#$@ mks 029 Data"

count_digit = 0
count_alpha = 0
count_sapce = 0
for i in ip:
    if i.isdigit():
        count_digit += 1
        print(i)
    elif i.isalpha():
        count_alpha += 1
    elif not i.isspace():
        count_sapce += 1

print(count_digit, count_alpha, count_sapce)
