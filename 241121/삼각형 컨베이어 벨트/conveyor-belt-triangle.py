n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

for _ in range(t):
    temp1 = arr[0][-1]
    for i in range(n - 1, 0, -1):
        arr[0][i] = arr[0][i - 1]
    temp2 = arr[1][-1]
    for i in range(n - 1, 0, -1):
        arr[1][i] = arr[1][i - 1]
    temp3 = arr[2][-1]
    for i in range(n - 1, 0, -1):
        arr[2][i] = arr[2][i - 1]
    
    arr[1][0] = temp1
    arr[2][0] = temp2
    arr[0][0] = temp3

for i in range(3):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
