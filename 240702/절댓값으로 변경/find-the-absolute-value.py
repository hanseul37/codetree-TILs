def value(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1

n = int(input())
arr = list(map(int, input().split()))
value(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")