arr2 = []
for i in range(4):
    arr = list(map(int, input().split()))
    arr2.append(arr)
for i in range(4):
    print(sum(arr2[i]))