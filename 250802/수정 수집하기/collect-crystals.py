n, k = map(int, input().split())
crystal = input()

# dp[i][j][l] = i번째까지 보고, 전환 j번 했고, 마지막이 l (0: L, 1: R)일 때 최대 길이
dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

dp[0][0][0] = 0
dp[0][0][1] = 0

for i in range(n):
    curr = 0 if crystal[i] == 'L' else 1
    for j in range(k + 1):
        for l in range(2):
            if dp[i][j][l] == -1:
                continue

            # 선택하지 않는 경우
            dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])

            # 같은 방향으로 이어 붙이기
            if l == curr:
                dp[i + 1][j][curr] = max(dp[i + 1][j][curr], dp[i][j][l] + 1)
            else:
                if j < k:
                    dp[i + 1][j + 1][curr] = max(dp[i + 1][j + 1][curr], dp[i][j][l] + 1)

    # 새로 시작하는 경우도 고려
    dp[i + 1][0][curr] = max(dp[i + 1][0][curr], 1)

# 정답 계산
max_crystal = 0
for j in range(k + 1):
    for l in range(2):
        if dp[n][j][l] != -1:
            max_crystal = max(max_crystal, dp[n][j][l])

print(max_crystal)
