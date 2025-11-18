n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value = -1000 * n * n
for top in range(n):
    temp = [0] * n
    for bottom in range(top, n):
        for col in range(n):
            temp[col] += arr[bottom][col]
        current_sum = 0
        for val in temp:
            current_sum = max(val, current_sum + val)
            max_value = max(max_value, current_sum)

print(max_value)
