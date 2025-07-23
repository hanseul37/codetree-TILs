n, k = map(int, input().split())
crystal = input()

# dp[i][j][l]: i까지 보고, j번 바꿨고, l==0이면 안 고르는 중, l==1이면 고르는 중
dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0  # 아무것도 안 고르고 시작

for i in range(n):
    curr = 0 if crystal[i] == 'L' else 1
    for j in range(k + 1):
        for l in range(2):
            if dp[i][j][l] == -1:
                continue

            # 1. 선택 안 하고 넘어감
            dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])

            if l == 0:
                # 2. 이전에 안 고르다가 이번에 선택 시작
                dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][0] + 1)
            else:
                # l == 1: 고르고 있는 중
                prev_type = 0 if crystal[i - 1] == 'L' else 1 if i > 0 else curr
                if curr == prev_type:
                    # 3. 같은 타입 계속 고름
                    dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][1] + 1)
                elif j < k:
                    # 4. 다른 타입으로 바꾸기
                    dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][1] + 1)

# 결과: 마지막까지 봤을 때, 최대 몇 개 고를 수 있는지
res = 0
for j in range(k + 1):
    for l in range(2):
        res = max(res, dp[n][j][l])
print(res)
