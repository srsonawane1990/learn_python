# Write a function to return list of all even numbers from given list

def even_nos(lst1):
    evens = []
    for i in lst1:
        if (i%2 == 0):
            evens.append(i)
    print(evens)

lst1 = [1,2,3,4,5,5,6,6,44,33,32]
even_nos(lst1)
