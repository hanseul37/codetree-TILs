word = input()
cnt = 0
for i in range(len(word) - 3):
    for j in range(i + 1, len(word) - 1):
        if word[i] == '(' and word[i + 1] == '(' and word[j] == ')' and word[j + 1] == ')':
            cnt += 1
print(cnt)