n = int(input())
for i in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    sum = 1
    for j in range(a, b+1):
        sum *= j
    print(sum)