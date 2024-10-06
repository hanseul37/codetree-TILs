n = int(input())
lines = []
for i in range(n):
    line = list(map(int, input().split()))
    lines.append(line)

min_len = 100
for i in range(n):
    copy_arr = lines.copy()
    copy_arr.pop(i)
    max_value, min_value = 0, 100
    for j in range(n - 1):
        if max_value < copy_arr[j][1]:
            max_value = copy_arr[j][1]
        if min_value > copy_arr[j][0]:
            min_value = copy_arr[j][0]
    if min_len > max_value - min_value:
        min_len = max_value - min_value   
print(min_len)