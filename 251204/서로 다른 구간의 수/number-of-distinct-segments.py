n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
point, cnt = arr[0][1], 1
for i in range(1, n):
    start, end = arr[i]
    if point < start:
        cnt += 1
    point = max(point, end)

print(cnt)