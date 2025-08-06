n, k = map(int, input().split())
arr = list(map(int, input().split()))
sums = {}
cnt = 0
for i in range(n):
    if k - arr[i] in sums:
        cnt += sums[k - arr[i]]
    for j in range(i):
        plus = arr[i] + arr[j]
        if plus not in sums:
            sums[plus] = 1
        else:
            sums[plus] += 1
print(cnt)

