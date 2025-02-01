word_dict = {}

file = open("sets\words.txt", "r")
words = file.readline().split(" ")
print(words)
file.close()

for word in words:
    count = words.count(word)
    word_dict[word] = count

print(word_dict)

print(max(word_dict, key=word_dict.get))