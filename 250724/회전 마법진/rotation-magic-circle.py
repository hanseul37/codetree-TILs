import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = input()
b = input()
dp = [[-1] * 10 for _ in range(n + 1)]

def dfs(cycle, rot):
    if cycle == n:
        return 0
    if dp[cycle][rot] != -1:
        return dp[cycle][rot]

    point = (int(a[cycle]) + rot) % 10
    target = int(b[cycle])

    cw = (target - point) % 10
    ccw = (point - target) % 10

    cost1 = dfs(cycle + 1, (rot + cw) % 10) + cw
    cost2 = dfs(cycle + 1, rot) + ccw

    dp[cycle][rot] = min(cost1, cost2)
    return dp[cycle][rot]

print(dfs(0, 0))


    

    


