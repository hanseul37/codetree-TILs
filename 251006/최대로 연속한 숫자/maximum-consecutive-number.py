from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = SortedList([[0, n]], key= lambda x: x[0])

for i in range(m):
    max_cnt = 0
    for elem in num:
        if elem[0] < arr[i] < elem[1]:
            num.remove(elem)
            num.add([elem[0], arr[i] - 1])
            num.add([arr[i] + 1, elem[1]])
            max_cnt = max(max_cnt, arr[i] - elem[0], elem[1] - arr[i])
            continue
        elif elem[0] == arr[i]:
            elem[0] += 1
        elif elem[1] == arr[i]:
            elem[1] -= 1
        max_cnt = max(max_cnt, elem[1] - elem[0] + 1)
    print(max_cnt)