in_file = open('lyrics.txt', 'r')
word_find = input("Please enter a word you would like to find: ")

word_count = 0
for line in in_file:
    words = line.split()
    for i in words:
        if word_find.lower() == i.lower():
            word_count += 1
print("The word: {} in {} appears {} times".format(word_find, in_file, word_count))
