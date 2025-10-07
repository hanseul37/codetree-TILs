from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key=lambda x: x[0])
length = SortedList([[n + 1, 0]], key=lambda x: -x[0])

for val in arr:
    if not num:
        print(0)
        continue

    idx = num.bisect_right([val, n + 1]) - 1
    l, r = num[idx]
    num.pop(idx)
    length.remove([r - l + 1, l])

    if l == val:
        if l + 1 <= r:
            num.add([l + 1, r])
            length.add([r - l, l + 1])
    elif r == val:
        if l <= r - 1:
            num.add([l, r - 1])
            length.add([r - l, l])
    else:
        if l <= val - 1:
            num.add([l, val - 1])
            length.add([val - l, l])
        if val + 1 <= r:
            num.add([val + 1, r])
            length.add([r - val, val + 1])

    if length:
        print(length[0][0])
    else:
        print(0)