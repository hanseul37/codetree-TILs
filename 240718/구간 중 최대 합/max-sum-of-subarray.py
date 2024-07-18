n, k = list(map(int, input().split()))
arr =  list(map(int, input().split()))

max_value = 0
for i in range(n - k + 1):
    sum = 0
    for j in range(i, i + k):
        sum += arr[j]
    max_value = max(max_value, sum)
print(max_value)