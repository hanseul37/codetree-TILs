n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_size = -1
for i in range(n):
    for j in range(m):
        for k in range(1, n - i + 1):
            for l in range(1, m - j + 1):
                cnt = 0
                flag = 0
                for a in range(i, i + k):
                    for b in range(j, j + l):
                        if arr[a][b] < 0:
                            flag = 1
                            break
                        else:
                            cnt += 1
                if flag == 0:
                    max_size = max(max_size, cnt)

print(max_size)

            