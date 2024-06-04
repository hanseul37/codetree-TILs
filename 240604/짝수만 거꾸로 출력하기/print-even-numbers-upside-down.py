n = int(input())
arr = list(map(int, input().split()))
ar = arr[::-1]
for i in range(n):
    if ar[i] % 2 == 0:
        print(ar[i], end=" ")