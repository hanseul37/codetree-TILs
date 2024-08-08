n, k = map(int, input().split())
arr = list(map(int, input().split()))

point = 0
values = arr[0]
while point < n - 1 :
    if point + k >= n - 1:
        values = max(arr[n - 1], values)
        break
    else:
        val = 100
        for i in range(point + 1, point + k + 1):
            if arr[i] < val:
                val = arr[i]
                point = i
        values = max(arr[point], values)
print(values)