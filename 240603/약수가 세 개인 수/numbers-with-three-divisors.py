arr = input().split()
start, end = int(arr[0]), int(arr[1])
cnt = 0
for i in range(start, end+1):
    sum = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum += 1
    if sum == 3:
        cnt += 1
print(cnt)