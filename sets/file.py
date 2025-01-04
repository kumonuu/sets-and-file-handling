file = open("file.txt", "w")
file.write("hello\n")
file.close()

file = open("file.txt", "a")
file.write("world\n")
file.write("my name is tim")
file.close()

file = open("file.txt", "r")
text_line = file.readline()
text_line2 = file.readline()
text_lines = file.readlines()
text_in_file = file.read()

print(text_in_file)
print(text_line)
# print(text_lines)
print(text_line2)