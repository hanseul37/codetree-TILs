from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = SortedList([[0, n]], key=lambda x: x[0])
lengths = SortedList([n - 0 + 1])  # 구간 길이들 관리

for x in arr:
    idx = num.bisect_left([x, 0]) - 1
    l, r = num[idx]
    length = r - l + 1
    
    # 기존 구간 제거
    num.pop(idx)
    lengths.remove(length)
    
    # 세 경우로 분기
    if l == r == x:
        pass  # 구간 완전히 사라짐
    elif l == x:
        num.add([x + 1, r])
        lengths.add(r - (x + 1) + 1)
    elif r == x:
        num.add([l, x - 1])
        lengths.add((x - 1) - l + 1)
    else:
        num.add([l, x - 1])
        num.add([x + 1, r])
        lengths.add((x - 1) - l + 1)
        lengths.add(r - (x + 1) + 1)
    
    print(lengths[-1] if lengths else 0)
