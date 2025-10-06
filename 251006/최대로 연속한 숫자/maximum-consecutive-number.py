from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key=lambda x: x[0])

# 현재 최대 길이
max_len = n

for x in arr:
    idx = num.bisect_left([x, 0]) - 1
    l, r = num[idx]
    
    # 구간 업데이트
    num.pop(idx)
    if l <= x - 1:
        num.add([l, x - 1])
    if x + 1 <= r:
        num.add([x + 1, r])
    
    # max_len 갱신
    max_len = max(max_len, max(r - l for l, r in num))
    print(max_len)
