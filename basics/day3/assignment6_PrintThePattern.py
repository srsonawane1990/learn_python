# Print following pattern
# *
# **
# ***
# ****
# *****

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(("*"), end=" ")
        j = j + 1
    i = i + 1
    print('')

