n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, 1])
    arr.append([e + 1, -1])
arr.sort()

max_cnt, cnt, day = 0, 0, 0
for d, v in arr:
    if d != day:
        max_cnt = max(cnt, max_cnt)
    cnt += v
    day = d
max_cnt = max(cnt, max_cnt)
print(max_cnt)


