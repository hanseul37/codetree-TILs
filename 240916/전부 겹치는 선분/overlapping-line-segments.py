n = int(input())
arr = [0] * 101

for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2 + 1):
        arr[j] += 1

find = 0
for i in range(101):
    if arr[i] == n:
        find = 1

if find:
    print('Yes')
else:
    print('No')