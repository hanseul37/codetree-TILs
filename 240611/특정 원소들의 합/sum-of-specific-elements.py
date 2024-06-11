arr2 = []
for i in range(4):
    arr = list(map(int, input().split()))
    arr2.append(arr)
total = 0
for i in range(4):
    for j in range(i+1):
        total += arr2[i][j]
print(total)