OFFSET = 1000
MAX_R = 2000
n = int(input())
point = 0
segments = []

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        left = point - distance
        right = point
        point = left
    else:
        left = point
        right = point + distance
        point = right

    segments.append([left, right])

coverage = [0] * (MAX_R + 1)

for left, right in segments:
    left += OFFSET
    right += OFFSET
    
    for i in range(left, right):
        coverage[i] += 1

count = sum(1 for x in coverage if x >= 2)

print(count)