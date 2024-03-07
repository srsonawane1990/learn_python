
list1=[-10, -8, 2, 4, 6]
# Ans ===> list2=[ 4, 16, 36, 64, 100]

list3 = []
j = 0
def data(list):
    if(len(list)!=0):
        for i in list:
            j = i * i
            list3.append(j)
        print(list3)
        print(sorted(list3))
    else:
        print("Input list is empty!!")

data(list1)

