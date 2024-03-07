#Write a program to count the occourance of chars in given paragraph

def count_occurances(paragraph):
    paragraph = paragraph.lower()
    char_count = {}
    for char in paragraph:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

paragraph = "This is a sample paragraph. It contains some charecotrs."
char_counts = count_occurances(paragraph)
print("Charector counts: ")
for char, count in char_counts.items():
    print(f"{char} : {count}")
