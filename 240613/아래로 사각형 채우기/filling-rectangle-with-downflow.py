n = int(input())
arr = []
for i in range(1, n+1):
    ar = []
    for j in range(n):
        ar.append(i + n * j)
    arr.append(ar)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()