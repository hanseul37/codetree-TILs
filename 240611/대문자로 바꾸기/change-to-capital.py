arr2 = []
for i in range(5):
    arr = input().split()
    arr2.append(arr)
for i in range(5):
    for j in range(3):
        print(arr2[i][j].upper(), end=" ")
    print()