n, b = list(map(int, input().split()))
students = []
for _ in range(n):
    student = list(map(int, input().split()))
    students.append(student)
students.sort()

max_cnt = 0
for i in range(n):
    sum_price = 0
    cnt = 0
    for j in range(n):
        if i == j:
            sum_price += students[j][0] // 2 + students[j][1]
        else:
            sum_price += students[j][0] + students[j][1]

        if sum_price > b:
            break
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)