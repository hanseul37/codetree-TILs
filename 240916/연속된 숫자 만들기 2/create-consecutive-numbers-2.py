arr = list(map(int, input().split()))
arr.sort()
if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
    print(0)
elif arr[0] + 2 == arr[1] or arr[1] + 2 == arr[2]:
    print(1)
else:
    print(2)