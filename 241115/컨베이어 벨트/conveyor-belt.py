n, t = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(t):
    temp1 = arr1[-1]
    temp2 = arr2[-1]
    arr1 = [temp2] + arr1[:-1]
    arr2 = [temp1] + arr2[:-1]

for i in range(n):
    print(arr1[i], end=' ')
print()
for i in range(n):
    print(arr2[i], end=' ')