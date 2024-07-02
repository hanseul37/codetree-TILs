def change(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2
    return arr

n = int(input())
arr = list(map(int, input().split()))
arr = change(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")