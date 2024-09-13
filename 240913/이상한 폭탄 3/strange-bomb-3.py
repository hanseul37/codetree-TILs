n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

max_cnt, bomb = 0, 0
for i in range(1000001):
    cnt, point = 0, 0
    while point < n:
        if arr[point] == i:
            if point + k < n:
                for j in range(point + 1, point + k + 1):
                    if arr[j] == i:
                        cnt += 1
                        point = j - 1
                        break
            else:
                if point == n - 1:
                    cnt += 1
                for j in range(point + 1, n):
                    if arr[j] == i:
                        cnt += 1
                        point = j - 1
                        break
        point += 1
    if cnt != 0:
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        bomb = i
print(bomb)