n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(items, idx, weight, value):
        if idx == len(items):
            if weight <= c:
                return value
            else:
                return 0
        exclude = dfs(items, idx + 1, weight, value)
        include = 0
        if weight + items[idx] <= c:
            include = dfs(items, idx + 1, weight + items[idx], value + items[idx] ** 2)
        return max(exclude, include)


item_values = [[0] * (n - m + 1) for _ in range(n)] 
for i in range(n):
    for j in range(n - m + 1): 
        items = arr[i][j:j + m] 
        item_values[i][j] = dfs(items, 0, 0, 0)

max_value = 0
for r1 in range(n): 
    for c1 in range(n - m + 1): 
        for r2 in range(r1, n): 
            if r1 == r2:
                for c2 in range(c1 + m, n - m + 1):
                    max_value = max(max_value, item_values[r1][c1] + item_values[r2][c2])
            else:
                for c2 in range(n - m + 1):
                    max_value = max(max_value, item_values[r1][c1] + item_values[r2][c2])
print(max_value)