n = input()
dp = [[0, 0] for _ in range(3)]
dp[0][0] = 1
for c in n:
    new_dp = [[0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(2):
            if not dp[i][j]:
                continue
            for k in range(10):
                if k in [3, 6, 9]:
                    continue
                if j == 0 and k > int(c):
                    continue
                new_dp[(i + k) % 3][j or k < int(c)] += dp[i][j]
    dp = new_dp
print((int(n) - sum(dp[1]) - sum(dp[2])) % (10**9 + 7))

                