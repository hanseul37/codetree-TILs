n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr1 = arr[:n]
arr2 = arr[n:]
min_value = 1000000000
for i in range(n):
    min_value = min(min_value, arr2[i] - arr1[i])
print(min_value)