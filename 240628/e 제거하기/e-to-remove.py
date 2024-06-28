word = list(input())
for i in range(len(word)):
    if word[i] == 'e':
        word.pop(i)
        break
print(''.join(word))