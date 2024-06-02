n = int(input())
for i in range(n, 0, -1):
    for j in range(n - i + 1):
        print(i+j, end=" ")
    for j in range(n-1):
        print(" ", end=" ")
    print()