x = int(input())

def check(speed, dist):
    for i in range(speed - 1, 0, -1):
        dist += i
    if dist > x:
        return False
    else:
        return True


speed = 2
dist = 3
time = 2
while speed > 1:
    if check(speed + 1, dist + speed + 1):
        speed += 1
        dist += speed
        time += 1
    elif check(speed, dist + speed):
        dist += speed
    else:
        speed -= 1
        dist += speed
        time += 1
print(time + 1)