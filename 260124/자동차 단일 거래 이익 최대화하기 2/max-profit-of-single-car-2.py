n = int(input())
price = list(map(int, input().split()))
max_diff, point = 0, price[0]
for i in range(1, n):
    if price[i] < price[i - 1]:
        point = min(price[i], point)
    else:
        max_diff = max(price[i] - point, max_diff)
print(max_diff)