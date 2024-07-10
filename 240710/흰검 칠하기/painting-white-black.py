n = int(input())
color = ['' for i in range(200000)]
point = 0

for _ in range(n):
    amount, direction = input().split()
    amount = int(amount)
    if direction == 'R':
        for i in range(amount):
            if color[point + 100000].count('B') >= 2 and color[point + 100000].count('W') >= 2:
                continue
            else:
                color[point + 100000] += 'B' 
            if i != amount - 1:
                point += 1 
    else:
        for i in range(amount):
            if color[point + 100000].count('B') >= 2 and color[point + 100000].count('W') >= 2:
                continue
            else:
                color[point + 100000] += 'W' 
            if i != amount - 1:
                point -= 1 

w, b, g = 0, 0, 0
for i in range(200000):
    if color[i] == '':
        continue
    elif color[i].count('B') == 2 and color[i].count('W') == 2:
        g += 1
    elif color[i][-1] == 'W':
        w += 1
    elif color[i][-1] == 'B':
        b += 1
print(w, b, g)