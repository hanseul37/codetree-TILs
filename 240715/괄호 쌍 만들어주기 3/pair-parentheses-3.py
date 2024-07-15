word = input()
cnt = 0
for i in range(len(word) - 1):
    for j in range(i + 1, len(word)):
        if word[i] == '(' and word[j] == ')':
            cnt += 1
print(cnt)