n = int(input())
arr = []
for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

def in_range(x, y, n):
    return x >= 0 and x < n and y >= 0 and y < n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 

cnt = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            if in_range(i + dx, j + dy, n) and arr[i + dx][j + dy] == 1:
                count += 1
        if count >= 3:
            cnt += 1

print(cnt)