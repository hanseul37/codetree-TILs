n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dp = [False] * (total + 1)
dp[0] = True

for num in arr:
    for j in range(total, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

diff = 1000 * n
for i in range(1, total):
    if dp[i]:
        a, b = i, total - i
        if a != 0 and b != 0:
            diff = min(diff, abs(a - b))
print(diff)
