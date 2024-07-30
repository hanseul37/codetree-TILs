n = int(input())
ices = []
for _ in range(n):
    h = int(input())
    ices.append(h)

max_cnt = 0
for i in range(1, max(ices)):
    cnt = 0
    if ices[0] - i <= 0:
        flag = 0
    else:
        cnt += 1
        flag = 1
    for j in range(n):
        if flag == 0:
            if ices[j] - i > 0:
                flag = 1
                cnt += 1
        else:
            if ices[j] - i <= 0:
                flag = 0
    max_cnt= max(max_cnt, cnt)

print(max_cnt)