n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    word = input()
    arr.append(word)

def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if in_range(j, i + 1, n, m) and in_range(j, i + 2, n, m) and arr[i + 1][j] == 'E' and arr[i + 2][j] == 'E':
                cnt += 1
            if in_range(j, i - 1, n, m) and in_range(j, i - 2, n, m) and arr[i - 1][j] == 'E' and arr[i - 2][j] == 'E':        
                cnt += 1
            if in_range(j + 1, i, n, m) and in_range(j + 2, i, n, m) and arr[i][j + 1] == 'E' and arr[i][j + 2] == 'E':
                cnt += 1
            if in_range(j - 1, i, n, m) and in_range(j - 2, i, n, m) and arr[i][j - 1] == 'E' and arr[i][j - 2] == 'E':
                cnt += 1
            if in_range(j + 1, i + 1, n, m) and in_range(j + 2, i + 2, n, m) and arr[i + 1][j + 1] == 'E' and arr[i + 2][j + 2] == 'E':
                cnt += 1
            if in_range(j - 1, i - 1, n, m) and in_range(j - 2, i - 2, n, m) and arr[i - 1][j - 1] == 'E' and arr[i - 2][j - 2] == 'E':
                cnt += 1
            if in_range(j + 1, i - 1, n, m) and in_range(j + 2, i - 2, n, m) and arr[i - 1][j + 1] == 'E' and arr[i - 2][j + 2] == 'E':
                cnt += 1
            if in_range(j - 1, i + 1, n, m) and in_range(j - 2, i + 2, n, m) and arr[i + 1][j - 1] == 'E' and arr[i + 2][j - 2] == 'E':
                cnt += 1
print(cnt)