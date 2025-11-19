n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]
alpha = {}
alpha['a'] = [[0] * m for _ in range(n)]
alpha['b'] = [[0] * m for _ in range(n)]
alpha['c'] = [[0] * m for _ in range(n)]
alphabet = ['a', 'b', 'c']

alpha[arr[0][0]][0][0] += 1
for i in range(1, n):
    for j in alphabet:
        alpha[j][i][0] = alpha[j][i - 1][0]
        if j == arr[i][0]:
            alpha[j][i][0] += 1
for i in range(1, m):
    for j in alphabet:
        alpha[j][0][i] = alpha[j][0][i - 1]
        if j == arr[0][i]:
            alpha[j][0][i] += 1
for i in range(1, n):
    for j in range(1, m):
        for l in alphabet:
            alpha[l][i][j] = alpha[l][i][j - 1] + alpha[l][i - 1][j] - alpha[l][i - 1][j - 1]
            if l == arr[i][j]:
                alpha[l][i][j] += 1

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    for i in alphabet:
        cnt = alpha[i][r2][c2]
        if r1 > 0:
            cnt -= alpha[i][r1 - 1][c2]
        if c1 > 0:
            cnt -= alpha[i][r2][c1 - 1]
        if r1 > 0 and c1 > 0:
            cnt += alpha[i][r1 - 1][c1 - 1]
        print(cnt, end = ' ')
    print()