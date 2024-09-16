n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] == b[i]:
        continue
    elif a[i] > b[i]:
        cnt += a[i] - b[i]
        a[i + 1] += a[i] - b[i]
print(cnt)