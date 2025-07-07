n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dp = [0] * (total + 1)
dp[0] = 1

for num in arr:
    for j in range(total, num - 1, -1):    
        if dp[j - num]:
            dp[j] += 1

max_sum = 0
for i in range(1, total):
    if dp[i] > 1:
        a, c = i, total - i * 2
        if c >= 0 and dp[c]:
            max_sum = max(max_sum, a)
print(max_sum)