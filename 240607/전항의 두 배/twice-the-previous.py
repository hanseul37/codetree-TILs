arr = input().split()
ar = [0] * 10
ar[0] = int(arr[0])
ar[1] = int(arr[1])
for i in range(2, 10):
    ar[i] = ar[i-1] + ar[i-2] * 2
for i in range(10):
    print(ar[i],end=" ")