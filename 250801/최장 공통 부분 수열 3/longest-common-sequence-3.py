n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i][j] = (LCS 길이, 해당 LCS 수열)
dp = [[(0, []) for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            length, seq = dp[i - 1][j - 1]
            dp[i][j] = (length + 1, seq + [a[i - 1]])
        else:
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j][0] < dp[i][j - 1][0]:
                dp[i][j] = dp[i][j - 1]
            else:
                # 길이가 같으면 사전순으로 앞선 수열 선택
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], key=lambda x: x[1])

# 결과 출력
result = dp[n][m][1]
print(*result if result else [])
