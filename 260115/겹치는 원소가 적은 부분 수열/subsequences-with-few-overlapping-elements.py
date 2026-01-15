n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, max_len, window = 0, 0, dict()
for right in range(n):
    if arr[right] in window:
        window[arr[right]] += 1
    else:
        window[arr[right]] = 1
    while window[arr[right]] > k:
        if window[arr[left]] == 1:
            del window[arr[left]]
        else:
            window[arr[left]] -= 1
        left += 1
    max_len = max(right - left + 1, max_len)
print(max_len)