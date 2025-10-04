n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n - 1, -1, -1):
    if k >= coins[i]:
        cnt += k // coins[i]
        k %= coins[i]
print(cnt)
