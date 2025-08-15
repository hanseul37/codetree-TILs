n = int(input())
hashset = set()
for _ in range(n):
    cmd, x = input().split()
    if cmd == 'add':
        hashset.add(x)
    elif cmd == 'remove':
        hashset.remove(x)
    else:
        if x in hashset:
            print('true')
        else:
            print('false')

