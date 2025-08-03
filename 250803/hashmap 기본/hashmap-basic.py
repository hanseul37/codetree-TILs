n = int(input())
commands = {}
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        commands[command[1]] = command[2]
    elif command[0] == 'remove':
        commands.pop(command[1])
    else:
        if command[1] in commands:
            print(commands[command[1]])
        else:
            print('None')
