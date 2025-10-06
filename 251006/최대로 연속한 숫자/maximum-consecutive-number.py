from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key= lambda x: x[0])

for i in range(m):
    idx = num.bisect_left([arr[i], 0]) - 1
    if num[idx][0] == arr[i]:
        num[idx][0] += 1
    elif num[idx][1] == arr[i]:
        num[idx][1] -= 1
    else:
        l, r = num[idx]
        num.pop(idx)
        num.add([l, arr[i] - 1])
        num.add([arr[i] + 1, r])
    
    max_cnt = 0
    for elem in num:
        max_cnt = max(max_cnt, elem[1] - elem[0] + 1)
    print(max_cnt)
