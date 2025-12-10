n = int(input())
arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, i, 1))
    arr.append((e, i, -1))

arr.sort()

computer = [0] * n
ans = [0] * n
next_free = 0

for time, person, flag in arr:
    if flag == 1:  # 들어오는 순간
        # next_free가 범위를 넘지 않도록 보장
        while next_free < n and computer[next_free] != 0:
            next_free += 1
        # 반드시 빈 자리가 있어야 함
        computer[next_free] = person
        ans[person] = next_free + 1

    else:  # 나가는 순간
        idx = ans[person] - 1
        computer[idx] = 0
        # next_free를 최소 위치로 되돌림
        if idx < next_free:
            next_free = idx

print(*ans)
