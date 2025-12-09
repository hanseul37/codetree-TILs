n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
max_len, cnt = 0, 0
start, end = arr[0][0], arr[0][1]
for a, b in arr:
    if a > end:
        max_len = max(cnt, max_len)
        start = a
    end = max(end, b)
    cnt = end - start
max_len = max(cnt, max_len)
print(max_len)
