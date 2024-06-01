arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(2, 9, 2):
    for j in range(b, a-1, -1):
        print(f'{j} * {i} = {j*i} ', end="")
        if j == a:
            break
        print('/', end=" ")
    print()