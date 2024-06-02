n = int(input())
for i in range(n, 0, -1):
    for j in range(0, 5-i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()