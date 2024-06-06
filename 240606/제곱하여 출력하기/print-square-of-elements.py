n = int(input())
arr = list(map(int, input().split()))
new = [i ** 2 for i in arr]
for i in range(n):
    print(new[i], end=" ")