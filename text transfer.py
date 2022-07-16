my_file = open("words2.txt", "r")
content = my_file.read().upper().replace("\n", " ")

my_file.close()
my_file = open("words.txt", "w")
my_file.writelines(content)
word_list = list(content.split("\n"))
print(word_list)
