arr = input().split()
n, m = int(arr[0]), int(arr[1])
ar = [
    [0 for i in range(n)]
    for _ in range(n)
]

for i in range(m):
    location = list(map(int, input().split()))
    ar[location[0] - 1][location[1] - 1] = 1

for i in range(n):
    for j in range(n):
        print(ar[i][j], end=" ")
    print()