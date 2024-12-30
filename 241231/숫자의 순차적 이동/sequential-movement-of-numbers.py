n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    for i in range(1, n * n + 1):
        flag = 0
        for a in range(n):
            for b in range(n):
                if arr[a][b] == i and flag == 0:
                    max_value = 0
                    r, c = -1, -1
                    for j in range(max(a - 1, 0), min(a + 2, n)):
                        for k in range(max(b - 1, 0), min(b + 2, n)):
                            if j == a and k == b:
                                continue
                            if arr[j][k] > max_value:
                                r = j
                                c = k
                                max_value = arr[j][k]
                    flag = 1
                    temp = arr[a][b]
                    arr[a][b] = arr[r][c]
                    arr[r][c] = temp

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()

                    
                    
                        
