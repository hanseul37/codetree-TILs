import sys
input = sys.stdin.readline

n, q = map(int, input().split())
visited, answers = [False] * (n + 1), []
for _ in range(q):
    dest = int(input())
    cur, ans = dest, 0
    while cur > 0:
        if visited[cur]:
            ans = cur
        cur //= 2
    if ans == 0:
        visited[dest] = True
        answers.append("0") 
    else:
        answers.append(str(ans)) 
print('\n'.join(answers))