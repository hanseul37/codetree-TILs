n, b = list(map(int, input().split()))
students = []
for _ in range(n):
    price = int(input())
    students.append(price)
students.sort()

max_cnt = 0
for i in range(n):
    sum_price = 0
    cnt = 0
    for j in range(n):
        if i == j:
            sum_price += students[j] // 2
        else:
            sum_price += students[j]
        cnt += 1
        
        if sum_price > b:
            cnt -= 1
            break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)