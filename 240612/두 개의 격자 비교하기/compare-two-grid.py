arr = input().split()
n, m = int(arr[0]), int(arr[1])
arr1 = []
arr2 = []
for _ in range(n):
    ar = list(map(int, input().split()))
    arr1.append(ar)
for _ in range(n):
    ar = list(map(int, input().split()))
    arr2.append(ar)
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()