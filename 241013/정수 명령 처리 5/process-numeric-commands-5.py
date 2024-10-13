n = int(input())
arr = []
for i in range(n):
    command = list(input().split())
    if command[0] == 'push_back':
        arr.append(command[1])
    elif command[0] == 'pop_back':
        arr.pop()
    elif command[0] == 'size':
        print(len(arr))
    else:
        print(arr[int(command[1]) - 1])