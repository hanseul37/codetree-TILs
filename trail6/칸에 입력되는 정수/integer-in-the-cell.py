n = int(input())
m = int(input())
k = [int(input()) for _ in range(m)]
arr = [i for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

ans = 0
for i in k:
    empty = find(i)
    if empty == 0: 
        break
    arr[empty] = empty - 1
    ans += 1
print(ans)



