n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, i + 1, 1])
    arr.append([end, i + 1, -1])
arr.sort()

computer, ans = [0] * n, [0] * n
for time, person, flag in arr:
    if flag == 1:
        for i in range(n):
            if computer[i] == 0:
                computer[i] = person
                ans[person - 1] = i + 1
                break
    else:
        computer[ans[person - 1] - 1] = 0
print(*ans)
