x = int(input())

def check(speed, dist):
    for i in range(speed - 1, 0, -1):
        dist += i
    if dist > x:
        return False
    else:
        return True


speed = 1
dist = 1
time = 1
while dist < x:
    if check(speed + 1, dist + speed + 1):
        speed += 1
        dist += speed
        time += 1
    elif check(speed, dist + speed):
        dist += speed
        time += 1
    else:
        speed -= 1
        dist += speed
        time += 1
print(time)