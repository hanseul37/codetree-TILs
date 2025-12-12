from sortedcontainers import SortedList

n = int(input())
arr = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    arr.append([x1, y, i, 1])   # start
    arr.append([x2, y, i, -1])  # end

# 정렬: x 증가, 같은 x라면 start(v=1) 먼저 처리하도록 (-v)
arr.sort(key=lambda e: (e[0], -e[3]))

cnt = 0
color = SortedList()

for x, y, idx, v in arr:
    # before 상태 저장
    before = color[0] if color else None

    if v == 1:
        color.add((y, idx))
    else:
        # 제거 (항상 존재한다고 가정)
        color.remove((y, idx))

    # after 상태 저장
    after = color[0] if color else None

    # 전면이 바뀌었으면 +1
    if before != after:
        cnt += 1

print(cnt)
