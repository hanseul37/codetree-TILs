n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dp = [False] * (total + 1)
dp[0] = True

for num in arr:
    for j in range(total, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

if total % 2 != 0 or not dp[total // 2]:
    print('No')
else:
    print('Yes')
