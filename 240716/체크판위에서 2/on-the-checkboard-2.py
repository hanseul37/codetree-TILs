r, c = list(map(int, input().split()))
arr = []
for _ in range(r):
    row = input().split()
    arr.append(row)

cnt = 0
for i in range(1, r - 2):
    for j in range(1, c - 2):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if arr[i][j] != arr[0][0] and arr[k][l] != arr[r - 1][c - 1] and arr[0][0] != arr[r - 1][c - 1]:
                    cnt += 1 
print(cnt)