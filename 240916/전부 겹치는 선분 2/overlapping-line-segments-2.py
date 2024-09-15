n = int(input())
lines = []
for i in range(n):
    line = list(map(int, input().split()))
    lines.append(line)

flag = 0
for i in range(n):
    arr = [0] * 101
    for j in range(n):
        if i == j:
            continue
        for k in range(lines[j][0], lines[j][1] + 1):
            arr[k] += 1
            if arr[k] == n - 1:
                flag = 1

if flag:
    print('Yes')
else:
    print('No')