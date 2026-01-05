n = int(input())
arr = list(map(int, input().split()))
min_diff = 2 * 10 ** 9
arr.sort()
left, right = 0, n - 1
sum_nums = arr[left] + arr[right]
while left < right:
    if arr[left] + arr[right] >= sum_nums:
        min_diff = min(sum_nums, min_diff)
        right -= 1
    else:
        min_diff = min(sum_nums, min_diff)
        left += 1
print(sum_nums)


