n, m = map(int, input().split())
arr = list(map(int, input().split()))
window, cnt, left = 0, 0, 0
for right in range(n):
    window += arr[right]
    while window > m:
        window -= arr[left]
        left += 1
    if window == m:
        cnt += 1
print(cnt)
        
