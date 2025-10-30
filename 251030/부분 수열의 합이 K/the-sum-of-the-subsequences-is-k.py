n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]
cnt = 0
for i in range(1, n + 1):
    for j in range(i):
        if prefix[i] - prefix[j] == k:
            cnt += 1
print(cnt)