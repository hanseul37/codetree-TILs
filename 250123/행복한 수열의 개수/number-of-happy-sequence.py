n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
happy_cnt = 0

for i in range(n):
    for j in range(n - m + 1):
        target = arr[i][j]
        flag = 1
        for k in range(j + 1, j + m):
            if arr[i][k] != target:
                flag = 0
                break
        if flag:
            happy_cnt += 1
            break

for i in range(n):
    for j in range(n - m + 1):
        target = arr[j][i]
        flag = 1
        for k in range(j + 1, j + m):
            if arr[k][i] != target:
                flag = 0
                break
        if flag:
            happy_cnt += 1
            break

print(happy_cnt)
        
