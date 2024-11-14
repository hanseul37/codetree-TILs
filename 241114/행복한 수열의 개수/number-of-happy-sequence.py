n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

happy = 0
for i in range(n):
    check = []
    for j in range(n):
        if arr[i][j] in check:
            happy += 1
            break
        else:
            if len(check):
                check.pop()
            check.append(arr[i][j])

for i in range(n):
    check = []
    for j in range(n):
        if arr[j][i] in check:
            happy += 1
            break
        else:
            if len(check):
                check.pop()
            check.append(arr[j][i])

print(happy)