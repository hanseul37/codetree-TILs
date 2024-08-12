n, k = map(int, input().split())
arr = []
for _ in range(n):
    bomb = int(input())
    arr.append(bomb)

max_cnt = 0
index = 0
for i in range(n):
    point = arr[i]
    cnt = 0
    location = []
    for j in range(n - 1):
        flag = 0
        if arr[j] == point:
            if j in location:
                flag = 1
            else:
                location.append(j)
            for k in range(j + 1, n):
                if arr[k] == point and k - j <= 3:
                    location.append(k)
                    if flag == 1:
                        cnt += 1
                    else:
                        cnt += 2
    if cnt > max_cnt:
        max_cnt = cnt
        index = point
print(index)