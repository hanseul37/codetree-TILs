n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    left, right = 0, n
    while left <= right:
        flag = False
        mid = (left + right) // 2
        if arr[mid] >= q:
            right = mid - 1
        else:
            left = mid + 1
    if arr[left] == q:
        print(left + 1)
    else:
        print(-1)

