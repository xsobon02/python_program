import random

output = ""
print("Guess the word!")
with open('words.txt') as f:
    for line in f:
        word_list = list(line.split(" "))
word = random.choice(word_list)


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
        if count[key] > 0:
            this_list.append(key)
            this_list.append(count[key])
    return this_list


word_letters = ''.join(str(x) for x in repeating_letters(word))
y = 1

while y <= 5:
    your_word = input().upper()
    your_word_letters = ''.join(str(x) for x in repeating_letters(your_word))
    output = []
    print(your_word_letters)
    if your_word in word_list:
        for x in range(5):
            if word[x] == your_word[x]:
                output.append("\033[1;32m" + your_word[x])
            elif word[x] != your_word[x]:
                output.append("x")
        for x in range(5):
            if word[x] == your_word[x]:
                continue
            elif word.__contains__(your_word[x]):
                if "\033[1;32m" + your_word[x] in output or "\033[1;33m" + your_word[x] in output and word_letters.__contains__(your_word_letters[0:2]) and word_letters[0:2].__contains__(your_word[x]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;33m" + your_word[x]]+output[i+1:]
                elif "\033[1;32m" + your_word[x] in output or "\033[1;33m" + your_word[x] in output and word_letters.__contains__(your_word_letters[2:4]) and word_letters[2:4].__contains__(your_word[x]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;33m" + your_word[x]]+output[i+1:]
                elif "\033[1;32m" + your_word[x] in output or "\033[1;33m" + your_word[x] in output and word_letters.__contains__(your_word_letters[4:6]) and word_letters[4:6].__contains__(your_word[x]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;33m" + your_word[x]]+output[i+1:]
                elif "\033[1;32m" + your_word[x] in output or "\033[1;33m" + your_word[x] in output and word_letters.__contains__(your_word_letters[6:8]) and word_letters[6:8].__contains__(your_word[x]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;33m" + your_word[x]]+output[i+1:]
                elif "\033[1;32m" + your_word[x] in output or "\033[1;33m" + your_word[x] in output and word_letters.__contains__(your_word_letters[8:10]) and word_letters[8:10].__contains__(your_word[x]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;33m" + your_word[x]]+output[i+1:]
                elif "\033[1;32m" + your_word[x] not in output and "\033[1;33m" + your_word[x] not in output:
                    i = output.index('x')
                    output = output[:i] + ["\033[1;33m" + your_word[x]] + output[i + 1:]
                elif your_word[x] in output and not word_letters.__contains__(your_word_letters[0:2]) or not word_letters.__contains__(your_word_letters[2:4]):
                    i = output.index('x')
                    output = output[:i]+["\033[1;31m" + your_word[x]]+output[i+1:]
                else:
                    i = output.index('x')
                    output = output[:i] + ["\033[1;31m" + your_word[x]] + output[i + 1:]
            else:
                i = output.index('x')
                output = output[:i] + ["\033[1;31m" + your_word[x]] + output[i + 1:]
        print_output = ''.join(str(x) for x in output)
        print(print_output)
        y += 1
        if your_word == word:
            print("\033[1;34mYou won!")
            exit()
    else:
        print("\033[1;37mWord not in word list.")
        continue
print(f"\033[1;35mYou lost. The word was \033[1;36m{word}\033[1;35m.")
