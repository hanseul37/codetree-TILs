n, t = list(map(int, input().split()))
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
direction = {
    'U': 0,
    'R': 1,
    "D": 2,
    'L': 3
}

change = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

for _ in range(t):
    if not in_range(c + dx[direction[d]], r + dy[direction[d]], n):
        d = change[d]
    else:
        r += dy[direction[d]]
        c += dx[direction[d]]

print(r + 1, c + 1)