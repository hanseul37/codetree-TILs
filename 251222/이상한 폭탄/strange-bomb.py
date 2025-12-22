n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
window = dict()
max_num = -1
for i in range(n):
    if i > k:
        window[arr[i - k - 1]] -= 1
    if arr[i] in window:
        window[arr[i]] += 1
    else:
        window[arr[i]] = 1
    if window[arr[i]] > 1:
        max_num = max(arr[i], max_num)
print(max_num)