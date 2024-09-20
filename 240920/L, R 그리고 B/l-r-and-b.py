arr = []
for i in range(10):
    line = list(input())
    arr.append(line)

L, R, B = [], [], [] 
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            L.append(i)
            L.append(j)
        elif arr[i][j] == 'R':
            R.append(i)
            R.append(j)
        elif arr[i][j] == 'B':
            B.append(i)
            B.append(j)

cnt = 0
point = [L[0], L[1]]
result1, result2 = 0, 0 
while not(point[0] == B[0] and point[1] == B[1]):
    if B[0] != point[0]:
        if B[0] < point[0]:
            if R[0] == point[0] - 1 and R[1] == point[1]:
                if B[1] > point[1]:
                    point[1] += 1
                else:
                    point[1] -= 1
            else:
                point[0] -= 1
        else:
            if R[0] == point[0] + 1 and R[1] == point[1]:
                if B[1] > point[1]:
                    point[1] += 1
                else:
                    point[1] -= 1
            else:
                point[0] += 1
    else:
        if B[1] < point[1]:
            if R[1] == point[1] - 1 and R[0] == point[0]:
                cnt = 100
                break
            else:
                point[1] -= 1
        else:
            if R[1] == point[1] + 1 and R[0] == point[0]:
                cnt = 100
                break
            else:
                point[1] += 1
    cnt += 1
        
result1 = cnt - 1

cnt = 0
point = [L[0], L[1]]
while not(point[0] == B[0] and point[1] == B[1]):
    if B[1] != point[1]:
        if B[1] < point[1]:
            if R[1] == point[1] - 1 and R[0] == point[0]:
                if B[0] > point[0]:
                    point[0] += 1
                else:
                    point[0] -= 1
            else:
                point[1] -= 1
        else:
            if R[1] == point[1] + 1 and R[0] == point[0]:
                if B[0] > point[0]:
                    point[0] += 1
                else:
                    point[0] -= 1
            else:
                point[1] += 1
    else:
        if B[0] < point[0]:
            if R[0] == point[0] - 1 and R[1] == point[1]:
                cnt = 100
                break
            else:
                point[0] -= 1
        else:
            if R[0] == point[0] + 1 and R[1] == point[1]:
                cnt = 100
                break
            else:
                point[0] += 1
    cnt += 1

result2 = cnt - 1
print(min(result1, result2))