n, m = list(map(int, input().split()))
a, b = [], []
a_point, b_point = 0, 0
for _ in range(n):
    direction, amount = input().split()
    amount = int(amount)
    if direction == 'L':
        for i in range(1, amount + 1):
            a_point -= 1
            a.append(a_point)
    else:
        for i in range(1, amount + 1):
            a_point += 1
            a.append(a_point)
    
for _ in range(m):
    direction, amount = input().split()
    amount = int(amount)
    if direction == 'L':
        for i in range(1, amount + 1):
            b_point -= 1
            b.append(b_point)
    else:
        for i in range(1, amount + 1):
            b_point += 1
            b.append(b_point)
    
for i in range(len(a)):
    if i != 0 and a[i] == b[i]:
        print(i + 1)
        break