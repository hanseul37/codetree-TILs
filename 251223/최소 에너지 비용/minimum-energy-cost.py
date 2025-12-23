n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost, total = 10 ** 6, 0
for i in range(n - 1):
    min_cost = min(cost[i], min_cost)
    total += min_cost * dist[i]
print(total)