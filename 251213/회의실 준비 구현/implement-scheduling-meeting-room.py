n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
cnt, point = 0, 0
for s, e in arr:
    if point <= s:
        cnt += 1
        point = e
print(cnt)
