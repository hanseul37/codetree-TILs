n, k = list(map(int, input().split()))
arr = [0] * 100000
for _ in range(n):
    location, alpha = input().split()
    if alpha == 'G':
        arr[int(location) - 1] = 1
    else:
        arr[int(location) - 1] = 2

max_value = 0
for i in range(10000 - k):
    sum = 0
    for j in range(k + 1):
        sum += arr[j]
    max_value = max(max_value, sum)

print(max_value)