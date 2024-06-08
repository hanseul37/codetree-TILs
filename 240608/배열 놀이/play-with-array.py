arr = input().split()
n, q = int(arr[0]), int(arr[1])
nn = list(map(int, input().split()))
for i in range(q):
    ar = list(map(int, input().split()))
    if ar[0] == 1:
        print(nn[ar[1]-1])
    elif ar[0] == 2:
        if ar[1] in nn:
            print(nn.index(ar[1]) + 1)
            break
        else:
            print(0)
    elif ar[0] == 3:
        for j in range(ar[1]-1, ar[2]):
            print(nn[j], end=" ")