n, b = list(map(int, input().split()))
students = []
for _ in range(n):
    p, s = map(int, input().split())
    students.append((p, s))

max_cnt = 0

for i in range(n):
    discounted_cost = (students[i][0] // 2) + students[i][1]
    other_costs = [(students[j][0] + students[j][1]) for j in range(n) if j != i]

    total_costs = sorted([discounted_cost] + other_costs)
    
    sum_price = 0
    cnt = 0
    
    for cost in total_costs:
        if sum_price + cost <= b:
            sum_price += cost
            cnt += 1
        else:
            break

    max_cnt = max(max_cnt, cnt)

print(max_cnt)