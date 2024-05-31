arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(a):
    for j in range(b):
        print((i+1)*(j+1), end=" ")
    print()