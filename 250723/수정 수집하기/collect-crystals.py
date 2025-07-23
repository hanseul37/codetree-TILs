n, k = map(int, input().split())
crystal = input()
dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

# 초기 선택 처리: i = 0 에서 시작한 선택은 j 증가 없이 해야 함
first = 0 if crystal[0] == 'L' else 1
dp[1][0][first] = 1  # 첫 문자 선택해서 시작

for i in range(1, n):
    curr = 0 if crystal[i] == 'L' else 1
    for j in range(k + 1):
        for l in range(2):
            # 그대로 진행 안 하고 넘기는 경우
            dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])
            
            if l == curr:
                # 같은 타입이면 그대로 선택
                dp[i + 1][j][curr] = max(dp[i + 1][j][curr], dp[i][j][l] + 1)
            else:
                # 다른 타입이면 전환 필요
                if j < k:
                    dp[i + 1][j + 1][curr] = max(dp[i + 1][j + 1][curr], dp[i][j][l] + 1)

max_crystal = 0
for j in range(k + 1):
    for l in range(2):
        max_crystal = max(max_crystal, dp[n][j][l])
print(max_crystal)
