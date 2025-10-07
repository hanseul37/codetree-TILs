from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key=lambda x: x[0])
length = SortedList([[n + 1, 0]], key=lambda x: -x[0])

for i in range(m):
    idx = num.bisect_left([arr[i], 0]) - 1
    l, r = num[idx]
    length.remove([r - l + 1, l])
    if l == arr[i]:
        num[idx][0] += 1
        length.add([r - l, l + 1])
    elif r == arr[i]:
        num[idx][1] -= 1
        length.add([r - l, l])
    else:
        num.pop(idx)
        num.add([l, arr[i] - 1])
        num.add([arr[i] + 1, r])
        length.add([arr[i] - l, l])
        length.add([r - arr[i], arr[i] + 1])

    print(length[0][0])


