N, M, D, S = list(map(int, input().split()))
people = [
    [0 for _ in range(101)]
    for i in range(N)
]
cheese = [0] * M

for _ in range(D):
    p, m, t = list(map(int, input().split()))
    people[p - 1][t] = m - 1

sicks = []
for _ in range(S):
    sick = list(map(int, input().split()))
    sicks.append(sick)

for i in range(M):
    for j in range(S):
        find = people[sicks[j][0]][:sicks[j][1]]
        if not i in find:
            break
    cheese[i] = 1

max_cnt = 0 
for i in range(M):
    cnt = 0
    if cheese[i] == 1:
        for j in range(N):
            if i in people[j]:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)