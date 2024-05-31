n = int(input())
for i in range(n):
    for j in range(n, 0, -1):
        print(j*(i+1), end=" ")
    print()