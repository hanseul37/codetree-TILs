n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bombs = [int(input()) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if arr[j][bombs[i] - 1] != 0:
            for k in range(arr[j][bombs[i] - 1]):
                if bombs[i] - 1 - k >= 0:
                    arr[j][bombs[i] - 1 - k] = 0
                if bombs[i] - 1 + k < n:
                    arr[j][bombs[i] - 1 + k]  = 0
                if j - k >= 0:
                    arr[j - k][bombs[i] - 1] = 0
                if j + k < n:
                    arr[j + k][bombs[i] - 1] = 0
            for k in range(n):
                non_zero = []
                for l in range(n):
                    if arr[l][k] != 0:
                        non_zero.append(arr[l][k])
                for l in range(n - len(non_zero)):
                    arr[l][k] = 0
                for l in range(n - len(non_zero), n):
                    arr[l][k] = non_zero[l - n + len(non_zero)]
            break

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()