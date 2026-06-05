import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [i for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y) 

cnt = n
for _ in range(m):
    a, b = map(int, input().split())
    point = find(a)
    while point < b:
        next_point = find(point + 1)
        union(point, next_point)
        cnt -= 1
        point = next_point
    print(cnt)
