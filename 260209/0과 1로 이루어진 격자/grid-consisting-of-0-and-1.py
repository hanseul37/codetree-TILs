n = int(input())
arr = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if arr[i][j] == '1':
            cnt += 1
            for y in range(i + 1):
                for x in range(j + 1):
                    arr[y][x] = str(1 - int(arr[y][x]))
print(cnt)