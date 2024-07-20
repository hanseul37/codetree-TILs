n, h, t = list(map(int, input().split()))
arr = list(map(int, input().split()))
min_cost = 20000
for i in range(n - t + 1):
    sum_cost = 0
    for j in range(i, i + t):
        sum_cost += abs(h - arr[j])
    min_cost = min(min_cost, sum_cost)

print(min_cost)