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

for cheese_type in range(M):
    is_sick_cheese = True
    for sick in sicks:
        sick_person = sick[0] - 1
        sick_time = sick[1]
        if not any(time < sick_time and m == cheese_type for time, m in people[sick_person]):
            is_sick_cheese = False
            break
    cheese[cheese_type] = 1 if is_sick_cheese else 0

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