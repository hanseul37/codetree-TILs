n = input()

def dfs(pos, mod, tight):
    if pos == len(n):
        if mod != 0:
            return 1
        else:
            return 0
    if tight:
        limit = int(n[pos])
    else:
        limit = 9
    res = 0
    for i in range(limit + 1):
        if i in [3, 6, 9]:
            continue
        new_tight = tight and i == limit
        res += dfs(pos + 1, (mod + i) % 3, new_tight)
    return res

print(int(n) - dfs(0, 0, True))