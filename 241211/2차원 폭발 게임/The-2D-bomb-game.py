n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(k + 1):
    for i in range(n):
        point = arr[0][i]
        cnt = 1
        j = 1
        while j < n:
            if arr[j][i] == 0:
                j += 1
                continue
            elif arr[j][i] == point:
                cnt += 1
            else:
                if cnt >= m:
                    for k in range(j - cnt, j):
                        arr[k][i] = 0
                    for a in range(n):
                        non_zero = []
                        for b in range(n):
                            if arr[b][a] != 0:
                                non_zero.append(arr[b][a])
                        for b in range(n - len(non_zero)):
                            arr[b][a] = 0
                        for b in range(n - len(non_zero), n):
                            arr[b][a] = non_zero[b - n + len(non_zero)]
                    j = 0
                point = arr[j][i]
                cnt = 1
            j += 1
        if cnt >= m:
            for k in range(n - cnt, n):
                arr[k][i] = 0
    
    for i in range(n):
        non_zero = []
        for j in range(n):
            if arr[j][i] != 0:
                non_zero.append(arr[j][i])
        for j in range(n - len(non_zero)):
            arr[j][i] = 0
        for j in range(n - len(non_zero), n):
            arr[j][i] = non_zero[j - n + len(non_zero)]
    
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[n - j - 1][i]
    arr = new_arr

    for i in range(n):
        non_zero = []
        for j in range(n):
            if arr[j][i] != 0:
                non_zero.append(arr[j][i])
        for j in range(n - len(non_zero)):
            arr[j][i] = 0
        for j in range(n - len(non_zero), n):
            arr[j][i] = non_zero[j - n + len(non_zero)]
    
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt += 1
print(cnt)