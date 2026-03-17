n, m, k = map(int, input().split())
dp = [[[-1] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]

def check(stone_idx, remain_num, min_val):
    if dp[stone_idx][remain_num][min_val] != -1:
        return dp[stone_idx][remain_num][min_val]
    elif stone_idx == n - 1:
        if remain_num == 0:
            return 1
        else:
            return 0
    elif remain_num <= 0 or min_val > remain_num:
        return 0
    cnt = 0
    for i in range(min_val, remain_num + 1):
        cnt += check(stone_idx + 1, remain_num - i, i)
    dp[stone_idx][remain_num][min_val] = cnt
    return cnt

ans, point = [], 1
for _ in range(n):
    for i in range(point, m + 1):
        cases = check(len(ans), m - i, i)
        if cases < k:
            k -= cases
        else:
            ans.append(i)
            m -= i
            point = i
            break
print(*ans)

