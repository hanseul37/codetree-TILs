x, y = list(map(int, input().split()))
cnt = 0
for i in range(x, y + 1):
    num = list(str(i))
    find = 1
    for j in range(len(num) // 2):
        if num[j] != num[-(j + 1)]:
            find = 0
            break
    if find:
        cnt += 1
print(cnt)