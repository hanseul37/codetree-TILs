n, k = map(int, input().split())
arr = list(map(int, input().split()))
nums = {}
cnt = 0
for num in arr:
    if k - num in nums:
        cnt += nums[k - num]
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1
print(cnt)

