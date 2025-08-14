from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))
sd = SortedDict()
for i in range(n):
    if arr[i] not in sd:
        sd[arr[i]] = i + 1
for key, value in sd.items():
    print(key, value)
