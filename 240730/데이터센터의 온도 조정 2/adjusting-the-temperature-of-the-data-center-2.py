n, c, g, h = list(map(int, input().split()))
temperatures = []
for _ in range(n):
    temperature = list(map(int, input().split()))
    temperatures.append(temperature)

max_operation = 0
for i in range(0, 1001):
    operation = 0
    for j in range(n):
        if i < temperatures[j][0]:
            operation += c
        elif temperatures[j][0] <= i <= temperatures[j][1]:
            operation += g
        else:
            operation += h
    max_operation = max(max_operation, operation)
print(max_operation)