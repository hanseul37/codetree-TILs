n = int(input())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and abs(j - l) < 3:
                    continue
                first = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                second = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                if max_cnt < first + second:
                    max_cnt = first + second

print(max_cnt)