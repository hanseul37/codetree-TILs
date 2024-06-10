arr = list(map(int, input().split()))
if arr[len(arr)-1] == 999:
    print(max(arr[:len(arr)-1]), min(arr))
elif arr[len(arr)-1] == -999:
    print(max(arr), min(arr[:len(arr)-1]))
else:
    print(max(arr), min(arr))