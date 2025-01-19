import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
num = list(map(int, input().split()))
visited = [n] * n
min_cnt = n + 1

def jump(location, cnt):
    global min_cnt
    if location >= n:
        return
    if location == n - 1:
        min_cnt = min(min_cnt, cnt)
        return
    if visited[location] <= cnt:
        return
    visited[location] = cnt
    for i in range(num[location] + 1):
        jump(location + i, cnt + 1)

jump(0, 0)

if min_cnt == n + 1:
    print(-1)
else:
    print(min_cnt)