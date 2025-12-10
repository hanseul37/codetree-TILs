n = int(input())
arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, i, 1))
    arr.append((e, i, -1))

arr.sort()

computer = [0]*n
ans = [0]*n
next_free = 0

for time, person, flag in arr:
    if flag == 1:  # 입장
        # next_free부터 가능한 곳을 찾기
        while computer[next_free] != 0:
            next_free += 1
        computer[next_free] = person
        ans[person] = next_free + 1
    else:  # 퇴장
        idx = ans[person] - 1
        computer[idx] = 0
        if idx < next_free:
            next_free = idx

print(*ans)
