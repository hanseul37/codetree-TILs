word = input()
cnt = 0
for i in range(len(word) - 1):
    if word[i] == 'e' and word[i+1] == 'e':
        cnt += 1
print(cnt, end=" ")
cnt = 0
for i in range(len(word) - 1):
    if word[i] == 'e' and word[i+1] == 'b':
        cnt += 1
print(cnt, end=" ")