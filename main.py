import random

output = ""
print("Guess the word!")
with open('words.txt') as f:
    for line in f:
        word_list = list(line.split(" "))
word = "SNAIL"#random.choice(word_list)


def repeating_letters(x):
    global y
    count = {}
    for s in x:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    this_list = []
    for key in count:
        if count[key] > 1:
            this_list.append(key)
            this_list.append(count[key])
    return this_list


word_letters = repeating_letters(word)
y = 1
while y <= 5:
    your_word = input().upper()
    your_word_letters = repeating_letters(your_word)
    if your_word in word_list:
        for x in range(5):
            if word[x] == your_word[x]:
                output = output + "\033[1;32m" + your_word[x]
            elif word.__contains__(your_word[x]):
                if your_word[x] not in output and word_letters.__contains__(your_word_letters[0:2]) or word_letters.__contains__(your_word_letters[2:4]):
                    output = output + "\033[1;33m" + your_word[x]
                elif output.__contains__(your_word[x]) and word_letters.__contains__(your_word_letters):
                    output = output + "\033[1;33m" + your_word[x]
                elif word.__contains__(your_word[x]):
                    output = output + "\033[1;33m" + your_word[x]
                else:
                    output = output + "\033[1;31m" + your_word[x]
            else:
                output = output + "\033[1;31m" + your_word[x]
        print(output)
        y += 1
        if your_word == word:
            print("\033[1;34mYou won!")
            exit()
    else:
        print("\033[1;37mWord not in word list.")
        continue
print(f"\033[1;35mYou lost. The word was \033[1;36m{word}\033[1;35m.")
