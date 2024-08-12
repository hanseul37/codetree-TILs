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
    for j in range(n - 1):
        if arr[j] == point:
            for k in range(j + 1, n):
                if arr[k] == point and k - j <= 3:
                    cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        index = point
print(index)