n, k = map(int, input().split())
arr = []
point = 0
for _ in range(n):
    m, d = input().split()
    if d == 'L':
        arr.append([point, -1])
        point -= int(m)
        arr.append([point, 1])
    else:
        arr.append([point, 1])
        point += int(m)
        arr.append([point, -1])
arr.sort()

prev, cur, cnt = None, 0, 0
for p, v in arr:
    if prev is not None and cur >= k:
        cnt += p - prev
    cur += v
    prev = p
print(cnt)