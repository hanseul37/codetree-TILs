arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(1, 10):
    for j in range(b, a-1, -2):
        print(f'{j} * {i} = {j*i} ', end="")
        if j == a:
            break
        print('/', end=" ")
    print()