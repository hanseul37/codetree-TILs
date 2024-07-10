n = int(input())
color = ['' for i in range(200000)]
point = 0
for _ in range(n):
    amount, direction = input().split()
    amount = int(amount)
    if direction == 'L':
        for i in range(amount):
            color[point + 100000] = 'W'
            if i + 1 == amount:
                break
            point -= 1
    else:
        for i in range(amount):
            color[point + 100000] = 'B'
            if i + 1 == amount:
                break
            point += 1

w = 0
b = 0
for i in range(200000):
    if color[i] == 'W':
        w += 1
    elif color[i] == 'B':
        b += 1

print(w, b)