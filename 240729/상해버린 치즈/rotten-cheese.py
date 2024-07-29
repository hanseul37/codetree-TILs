N, M, D, S = list(map(int, input().split()))

people = [set() for _ in range(N)]
cheese = [0] * M

for _ in range(D):
    p, m, t = list(map(int, input().split()))
    people[p - 1].add((t, m - 1))

sicks = []
for _ in range(S):
    sick = list(map(int, input().split()))
    sicks.append(sick)

for i in range(M):
    is_sick_cheese = False
    for sick in sicks:
        for time, cheese_type in people[sick[0] - 1]:
            if time < sick[1] and cheese_type == i:
                is_sick_cheese = True
                break
        if not is_sick_cheese:
            break
    if is_sick_cheese:
        cheese[i] = 1
    else:
        cheese[i] = 0

max_cnt = 0
for i in range(M):
    if cheese[i] == 1:
        cnt = 0
        for j in range(N):
            for _, cheese_type in people[j]:
                if cheese_type == i:
                    cnt += 1
                    break
        max_cnt = max(max_cnt, cnt)

print(max_cnt)