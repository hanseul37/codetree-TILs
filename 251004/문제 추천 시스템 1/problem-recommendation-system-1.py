from sortedcontainers import SortedSet

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
s = SortedSet(arr, key=lambda x: (x[1], x[0]))

m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'rc':
        if cmd[1] == '1':
            print(s[-1][0])
        else:
            print(s[0][0])
    elif cmd[0] == 'ad':
        s.add((int(cmd[1]), int(cmd[2])))
    else:
        s.discard((int(cmd[1]), int(cmd[2])))
