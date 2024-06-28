A = input()
command = input()
for i in range(len(command)):
    if command[i] == 'L':
        A = A[1:] + A[0]
    elif command[i] == 'R':
        A = A[-1] + A[:-1]
print(''.join(A))