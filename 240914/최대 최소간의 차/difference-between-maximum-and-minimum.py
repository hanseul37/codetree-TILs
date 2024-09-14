n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = 10000
for i in range(min(arr), max(arr) - k + 1):
    diff = 0
    for j in range(n):
        if arr[j] < i:
            diff += i - arr[j]
        elif arr[j] > i + k:
            diff += arr[j] - i - k
    min_diff = min(min_diff, diff)  
print(min_diff)