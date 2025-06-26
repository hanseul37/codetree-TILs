n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
cnt, end = 0, 0
for x1, x2 in arr:
    if end < x1:
        cnt += 1
        end = x2
print(cnt)