n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max = 0
for i in range(len(arr) // 2):
    if arr[i] + arr[-i] > max:
        max = arr[i] + arr[-i]
print(max)