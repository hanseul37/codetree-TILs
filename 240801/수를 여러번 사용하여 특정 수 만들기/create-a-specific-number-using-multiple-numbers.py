a, b, c = list(map(int, input().split()))
max_value = 0
for i in range(1000):
    for j in range(1000):
        value = a * i + b * j
        if value > max_value and value <= c:
            max_value = value
print(max_value)