n, m, k = map(int, input().split())
arr = [int(i) for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[find(v1)] = find(v2)
    
route = list(map(int, input().split()))
ans = 1
for i in range(k - 1):
    if find(route[i]) != find(route[i + 1]):
        ans = 0
print(ans)









