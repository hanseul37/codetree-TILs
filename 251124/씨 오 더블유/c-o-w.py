n = int(input())
arr = input()
c, w = [0] * n, [0] * n
for i in range(1, n):
    c[i] = c[i - 1]
    w[n - 1 - i] = w[n - i]
    if arr[i - 1] == 'C':
        c[i] += 1
    if arr[n - i] == 'W':
        w[n - 1 - i] += 1

cnt = 0
for i in range(1, n - 1):
    if arr[i] == 'O':
        cnt += c[i] * w[i]
print(cnt)
