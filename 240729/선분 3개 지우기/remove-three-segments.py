n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            arr = [0] * 101
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                for m in range(points[l][0], points[l][1] + 1):
                    arr[m] += 1
            
            flag = 0
            for l in range(101):
                if arr[l] > 1:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
                
print(cnt)