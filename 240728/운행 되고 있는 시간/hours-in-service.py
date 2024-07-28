n = int(input())
worker = []
for _ in range(n):
    time = list(map(int, input().split()))
    worker.append(time)

max_time = 0
for i in range(n):
    work_time = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        for k in range(worker[j][0], worker[j][1]):
            work_time[k] += 1

    cnt = 0
    for j in range(1001):
        if work_time[j] != 0:
            cnt += 1
    max_time = max(max_time, cnt)
print(max_time)