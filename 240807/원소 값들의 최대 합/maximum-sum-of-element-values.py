n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
max_sum = 0
for i in range(n):
    sum = 0
    point = i
    for j in range(m):
        sum += arr[point]
        point = arr[point] - 1
    max_sum = max(max_sum, sum)
print(max_sum)