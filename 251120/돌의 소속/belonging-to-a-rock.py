n, q = map(int, input().split())
arr = [int(input()) for _ in range(n)]
prefix = [[0] * n for _ in range(3)]
prefix[arr[0] - 1][0] += 1
for i in range(1, n):
    for j in range(3):
        prefix[j][i] = prefix[j][i - 1]
        if arr[i] - 1 == j:
            prefix[j][i] += 1

for _ in range(q):
    a, b = map(int, input().split())
    for i in range(3):
        ans = prefix[i][b - 1]
        if a > 1:
            ans -= prefix[i][a - 2]
        print(ans, end = ' ')
    print()
