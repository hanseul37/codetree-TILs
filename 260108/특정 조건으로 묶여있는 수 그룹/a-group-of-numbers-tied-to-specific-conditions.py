n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
cnt = [0] * n
right = 0 
for left in range(n):
    while right < n and nums[right] - nums[left] <= k:
        right += 1
    cnt[left] = right - left

right_max = [0] * n
right_max[-1] = cnt[-1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], cnt[i])

max_cnt = 0
for i in range(n):
    max_cnt = max(cnt[i] + right_max[i + cnt[i] - 1], max_cnt)
print(max_cnt)