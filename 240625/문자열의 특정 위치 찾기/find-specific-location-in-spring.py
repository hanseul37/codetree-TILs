arr = input().split()
if arr[1] in arr[0]:
    print(arr[0].index(arr[1]))
else:
    print('No')