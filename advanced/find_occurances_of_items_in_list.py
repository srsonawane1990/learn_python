def count_occurance(lst1):
    occrances = {}
    for item in lst1:
        if item in occrances:
            occrances[item] += 1
        else:
            occrances[item] = 1
    return occrances

lst1 = [1,2,3,2,3,44,5,23,23,22,3,4,2,3]

occrances = count_occurance(lst1)

for item, count in occrances.items():
    print(f"{item}: {count} occurances ")
