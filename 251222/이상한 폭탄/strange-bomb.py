from collections import deque

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
window = deque()
max_num = -1
for i in range(n):
    if i > k:
        window.popleft()
    if arr[i] in window:
        max_num = max(arr[i], max_num)
    window.append(arr[i])
print(max_num)