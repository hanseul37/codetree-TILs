n = int(input())
point = 0
arr = [0 for i in range(2000)]
for _ in range(n):
    x, dir = input().split()
    if dir == 'L':
        for i in range(point - 1, point - int(x) - 1, -1):
            arr[i + 1000] += 1
        point -= int(x)
    else:
        for i in range(point + 1, point + int(x) + 1, 1):
            arr[i + 1000] += 1
        point += int(x)

cnt = 0
flag = 0
for i in range(2000):
    if arr[i] >= 2:
        cnt += 1
print(cnt)