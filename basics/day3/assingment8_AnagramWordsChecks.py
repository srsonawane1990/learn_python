# anagram words check

s1 = input("Enter the 1st word: ")
s2 = input("Enter the 2nd word: ")
w1 = sorted(s1)
w2 = sorted(s2)
print("Enter the sorted words w1 = {} & w2 = {}".format(w1,w2))

if w1 == w2:
    print("Words are anagrams")
else:
    print("Words are not anagrams.")
