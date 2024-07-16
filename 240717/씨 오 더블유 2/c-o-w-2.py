n = int(input())
word = input()

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if word[i] == 'C' and word[j] == 'O' and word[k] == 'W':
                cnt += 1
print(cnt)