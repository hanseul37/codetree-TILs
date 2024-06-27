word = input()
word_list = list(word)
first = word_list[0]
second = word_list[1]
for i in range(len(word_list)):
    if word_list[i] == second:
        word_list[i] = first
word = "".join(word_list)
print(word)