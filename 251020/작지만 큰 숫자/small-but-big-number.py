from sortedcontainers import SortedList

n, m = map(int, input().split())
arr = SortedList(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    idx = arr.bisect_right(q) - 1
    if idx >= 0:
        print(arr.pop(idx))
    else:
        print(-1)
