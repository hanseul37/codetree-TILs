n, m = map(int, input().split())
arr = [int(i) for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for _ in range(m):
    menu, a, b = map(int, input().split())
    if menu == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)








