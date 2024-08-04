n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

m = n
for i in range(2, 100, 2):
    for j in range(2, 100, 2):
        cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
        for k in range(n):
            if points[k][0] > j and points[k][1] > i:
                cnt1 += 1
            elif points[k][0] < j and points[k][1] > i:
                cnt2 += 1
            elif points[k][0] < j and points[k][1] < i:
                cnt3 += 1
            elif points[k][0] > j and points[k][1] < i:
                cnt4 += 1
        max_cnt = max(cnt1, cnt2, cnt3, cnt4)
        m = min(m, max_cnt)

print(m)