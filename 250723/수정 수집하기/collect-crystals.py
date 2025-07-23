n, k = map(int, input().split())
crystal = input()

dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

# 초기값 설정: 아직 아무것도 안 고른 상태는 0으로 셋팅
dp[0][0][0] = 0
dp[0][0][1] = 0

for i in range(n):
    curr = 0 if crystal[i] == 'L' else 1
    for j in range(k + 1):
        for l in range(2):
            if dp[i][j][l] == -1:
                continue
            # 현재 상태 유지 (스킵)
            dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])

            if l == curr:
                # 같은 타입을 선택하는 경우
                dp[i + 1][j][curr] = max(dp[i + 1][j][curr], dp[i][j][l] + 1)
            else:
                # 다른 타입으로 바꾸는 경우 (횟수 제한 내에서)
                if j < k:
                    dp[i + 1][j + 1][curr] = max(dp[i + 1][j + 1][curr], dp[i][j][l] + 1)

max_crystal = 0
for j in range(k + 1):
    for l in range(2):
        max_crystal = max(max_crystal, dp[n][j][l])

print(max_crystal)
