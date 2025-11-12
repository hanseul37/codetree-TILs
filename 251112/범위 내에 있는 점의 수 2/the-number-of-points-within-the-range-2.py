n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
prefix = [0] * 1000001
cnt = 0
for i in range(1000001):
    if cnt < n and arr[cnt] == i:
        cnt += 1
    prefix[i] = cnt

for _ in range(q):
    a, b = map(int, input().split())
    if a == 0:
        print(prefix[b])
    else:
        print(prefix[b] - prefix[a - 1])
