n, m = map(int, input().split())
arr = [int(i) for i in range(n + 1)]
ans = ''

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

for i in range(1, m + 1):
    v1, v2 = map(int, input().split())
    if find(v1) == find(v2):
        ans = str(i)
        break
    arr[find(v1)] = find(v2)

if ans == '':
    print('happy')
else:
    print(ans)