n, m, p = map(int, input().split())
messages = []
for i in range(m):
    message = input().split()
    message[0] = ord(message[0])
    message[1] = int(message[1])
    messages.append(message)

programmers = [65 + i for i in range(n)]

for i in range(p - 1, m):
    if messages[i][0] in programmers:
        programmers.remove(messages[i][0])

for i in range(len(programmers)):
    print(chr(programmers[i]), end=' ')