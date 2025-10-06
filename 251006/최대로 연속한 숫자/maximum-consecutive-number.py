from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = [i for i in range(0, n + 1)]
num_set = SortedSet(num)

for i in range(m):
    num_set.remove(arr[i])
    max_cnt, cnt, target = 0, 0, -1
    for elem in num_set:
        if target + 1 == elem:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        target = elem
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)

