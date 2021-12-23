# text = "This is my first test.\nThis is next line.\nThis is last line."
# print(text)

# my_file = open("my file.txt", "w")
# my_file.write(text)
# my_file.close()

# append_text = "\nThis is append file."

# my_file = open("my file.txt", "a")
# my_file.write(append_text)
# my_file.close()

file = open("../my file.txt", "r")
content = file.read()
print(content)