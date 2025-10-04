n = int(input())
arr = list(map(int, input().split()))
max_value, cnt = -1000, 0
for elem in arr:
    cnt += elem
    max_value = max(max_value, cnt)
    if cnt < 0:
        cnt = 0
print(max_value)