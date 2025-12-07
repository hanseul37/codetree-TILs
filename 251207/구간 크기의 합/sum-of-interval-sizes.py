n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

arr.sort()
start, end = arr[0][0], arr[0][1]
for a, b in arr:
    if a > end:
        ans += end - start 
        start = a
    end = max(end, b)
ans += end - start
print(ans)