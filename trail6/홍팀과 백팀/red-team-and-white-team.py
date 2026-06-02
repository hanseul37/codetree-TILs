n, m = map(int, input().split())
arr = [i for i in range(2 * n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

ans = 1
for _ in range(m):
    v1, v2 = map(int, input().split())
    if find(v1) == find(v2) or find(v1 + n) == find(v2 + n):
        ans = 0
        break
    union(v1, v2 + n)
    union(v2, v1 + n)
print(ans)