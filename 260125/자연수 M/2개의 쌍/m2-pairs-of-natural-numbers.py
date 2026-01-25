n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])
arr.sort()
l, r, c = 0, n - 1, 0
while l <= r:
    if l == r:
        c = max(c, arr[l][0] * 2)
        break

    k = min(arr[l][1], arr[r][1])
    if k == 0:
        if arr[l][1] == 0:
            l += 1
        if arr[r][1] == 0:
            r -= 1
        continue

    c = max(c, arr[l][0] + arr[r][0])
    arr[l][1] -= k
    arr[r][1] -= k

    if arr[l][1] == 0:
        l += 1
    if arr[r][1] == 0:
        r -= 1

print(c)