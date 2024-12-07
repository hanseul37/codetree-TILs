arr = [list(map(int, input().split())) for _ in range(4)]
direction = input()

if direction == 'L':
    for i in range(4):
        non_zero, zero = [], []
        for j in range(4):
            if arr[i][j] == 0:
                zero.append(arr[i][j])
            else:
                non_zero.append(arr[i][j])
        for j in range(len(non_zero)):
            arr[i][j] = non_zero[j]
        for j in range(len(non_zero), 4):
            arr[i][j] = 0
    for i in range(4):
        for j in range(3):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] = arr[i][j] * 2
                for k in range(j + 1, 3):
                    arr[i][k] = arr[i][k + 1]
                arr[i][-1] = 0
    
elif direction == 'R':
    for i in range(4):
        non_zero, zero = [], []
        for j in range(4):
            if arr[i][j] == 0:
                zero.append(arr[i][j])
            else:
                non_zero.append(arr[i][j])
        for j in range(len(zero)):
            arr[i][j] = 0
        for j in range(len(zero), 4):
            arr[i][j] = non_zero[j - len(zero)]
    for i in range(4):
        for j in range(3, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] = arr[i][j] * 2
                for k in range(j - 1, 0, -1):
                    arr[i][k] = arr[i][k - 1]
                arr[i][0] = 0

elif direction == 'U':
    for i in range(4):
        non_zero, zero = [], []
        for j in range(4):
            if arr[j][i] == 0:
                zero.append(arr[j][i])
            else:
                non_zero.append(arr[j][i])
        for j in range(len(non_zero)):
            arr[j][i] = non_zero[j]
        for j in range(len(non_zero), 4):
            arr[j][i] = 0
    for i in range(4):
        for j in range(3):
            if arr[j][i] == arr[j + 1][i]:
                arr[j][i] = arr[j][i] * 2
                for k in range(j + 1, 3):
                    arr[k][i] = arr[k + 1][i]
                arr[-1][i] = 0

elif direction == 'D':
    for i in range(4):
        non_zero, zero = [], []
        for j in range(4):
            if arr[j][i] == 0:
                zero.append(arr[j][i])
            else:
                non_zero.append(arr[j][i])
        for j in range(len(zero)):
            arr[j][i] = 0
        for j in range(len(zero), 4):
            arr[j][i] = non_zero[j - len(zero)]
    for i in range(4):
        for j in range(3, 0, -1):
            if arr[j][i] == arr[j - 1][i]:
                arr[j][i] = arr[j][i] * 2
                for k in range(j - 1, 0, -1):
                    arr[k][i] = arr[k - 1][i]
                arr[0][i] = 0

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()