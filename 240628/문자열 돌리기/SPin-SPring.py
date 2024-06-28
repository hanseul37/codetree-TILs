word = input()
print(word)
for i in range(len(word)):
    word = word[-1] + word[:-1]
    print(word)