from copy import deepcopy

n, m, r, c = map(int, input().split())
arr = [[0] * n for _ in range(n)]
arr[r - 1][c - 1] = 1

for i in range(m):
    copy_arr = deepcopy(arr)
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1:
                if a - (i + 1) >= 0:
                    copy_arr[a - (i + 1)][b] = 1
                if b - (i + 1) >= 0:
                    copy_arr[a][b - (i + 1)] = 1
                if a + (i + 1) < n:
                    copy_arr[a + (i + 1)][b] = 1
                if b + (i + 1) < n:
                    copy_arr[a][b + (i + 1)] = 1
    arr = copy_arr

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)