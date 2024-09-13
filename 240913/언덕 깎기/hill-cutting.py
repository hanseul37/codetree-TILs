n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

min_cost = 100 * 100
for i in range(min(arr), max(arr) + 1):
    cost = 0
    for j in range(n):
        if not i <= arr[j] <= i + 17:
            if arr[j] < i:
                cost += (arr[j] - i) * (arr[j] - i)
            else:
                cost += (arr[j] - i - 17) * (arr[j] - i - 17)

    min_cost = min(min_cost, cost)
print(min_cost)