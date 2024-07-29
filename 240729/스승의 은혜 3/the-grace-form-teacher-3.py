n, b = list(map(int, input().split()))
students = []
for _ in range(n):
    student = list(map(int, input().split()))
    students.append(student)

max_cnt = 0
for i in range(n):
    discount = students[i][0] // 2 + students[i][1]
    other = [(students[j][0] + students[j][1]) for j in range(n) if i != j]

    total_costs = sorted([discount] + other)

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