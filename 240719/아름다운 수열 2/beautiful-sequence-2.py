n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(len(a) - len(b) + 1):
    flag = 0
    for j in range(i, i + len(b)):
        if not a[j] in b:
            flag = 1
            break
    for j in range(len(b)):
        if not b[j] in a[i:i + len(b)]:
            flag = 1
            break 
    if not flag:
        cnt += 1
print(cnt)