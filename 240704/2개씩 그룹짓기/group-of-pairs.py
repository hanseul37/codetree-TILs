n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max = 0
for i in range(len(arr) // 2 + 1):
    if arr[i] + arr[-i] > max:
        max = arr[i] + arr[-(i + 1)]
print(max)