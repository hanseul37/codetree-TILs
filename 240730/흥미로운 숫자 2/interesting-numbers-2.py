import statistics

x, y = list(map(int, input().split()))
sum_cnt = 0
for i in range(x, y + 1):
    d = list(map(int, str(i)))

    cnt = 0
    for j in range(len(d)):
        if d[j] != statistics.mode(d):
            cnt += 1
    if cnt == 1:
        sum_cnt += 1
print(sum_cnt)