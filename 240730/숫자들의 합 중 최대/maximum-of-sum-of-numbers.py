x, y = list(map(int, input().split()))
max_sum = 0
for i in range(x, y + 1):
    d = list(map(int, str(i)))
    cur_sum = sum(d)
    max_sum = max(max_sum, cur_sum)

print(max_sum)