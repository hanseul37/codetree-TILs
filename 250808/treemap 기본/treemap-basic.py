from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    line = input().split()
    cmd = line[0]
    
    if cmd == "add":
        key = int(line[1])
        value = int(line[2])
        sd[key] = value
    
    elif cmd == "remove":
        key = int(line[1])
        sd.pop(key, None)
    
    elif cmd == "find":
        key = int(line[1])
        print(sd.get(key, 'None'))
    
    elif cmd == "print_list":
        if sd:
            print(" ".join(map(str, sd.values())))
        else:
            print('None')
