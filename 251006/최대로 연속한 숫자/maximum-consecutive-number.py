from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key= lambda x: x[0])
point, max_cnt = 0, 0

for i in range(m):
    idx = num.bisect_left([arr[i], 0]) - 1    
    l, r = num[idx]
    if l == arr[i]:
        num[idx][0] += 1
    elif r == arr[i]:
        num[idx][1] -= 1
    else:
        num.pop(idx)
        num.add([l, arr[i] - 1])
        num.add([arr[i] + 1, r])
    
    if point == l:
        max_cnt = 0
        for elem in num:
            if elem[1] - elem[0] + 1 > max_cnt:
                max_cnt = elem[1] - elem[0] + 1
                point = elem[0]
    print(max_cnt)

