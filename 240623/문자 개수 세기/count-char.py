word = input()
cha = input()
cnt = 0
for i in range(len(word)):
    if word[i] == cha:
        cnt += 1
print(cnt)