ar = input().split()
arr = [0] * 10
arr[0] = int(ar[0])
arr[1] = int(ar[1])
for i in range(2, 10):
    arr[i] = (arr[i-2]+arr[i-1])%10
for i in range(10):
    print(arr[i], end=" ")