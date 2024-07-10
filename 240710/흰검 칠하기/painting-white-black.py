n = int(input())
color = ['' for i in range(200000)]
point = 0
last_direction = ''

for _ in range(n):
    amount, direction = input().split()
    amount = int(amount)
    if direction == 'R':
        if last_direction == 'R':
            point += 1
        for i in range(amount):
            if color[point + 100000] == 'W':
                color[point + 100000] = 'GB'
            elif color[point + 100000] == 'GW':
                color[point + 100000] = 'GGB'
            elif color[point + 100000] == 'GGW':
                color[point + 100000] = 'G'
            elif color[point + 100000] == 'G':
                continue
            else:
                color[point + 100000] = 'B' 
            if i != amount - 1:
                point += 1 
    else:
        if last_direction == 'L':
            point += 1
        for i in range(amount):
            if color[point + 100000] == 'B':
                color[point + 100000] = 'GW'
            elif color[point + 100000] == 'GB':
                color[point + 100000] = 'GGW'
            elif color[point + 100000] == 'GGB':
                color[point + 100000] = 'G'      
            elif color[point + 100000] == 'G':
                continue
            else:
                color[point + 100000] = 'W' 
            if i != amount - 1:
                point -= 1 
    last_direction = direction

w, b, g = 0, 0, 0
for i in range(200000):
    if color[i] == '':
        continue
    elif color[i][-1] == 'W':
        w += 1
    elif color[i][-1] == 'B':
        b += 1
    else:
        g += 1
print(w, b, g)