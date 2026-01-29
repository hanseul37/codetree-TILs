n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x:x[1])
cnt, point = 0, 0
for s, e in meetings:
    if s < point:
        cnt += 1
    else:
        point = e
print(cnt)