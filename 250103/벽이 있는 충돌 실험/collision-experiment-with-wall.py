from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = []
    for _ in range(m):
        r, c, d = input().split()
        beads.append((int(r) - 1, int(c) - 1, d))

    for _ in range(2 * n):
        next_positions = defaultdict(list)  # 위치별로 구슬을 그룹화
        for bead in beads:
            r, c, d = bead
            if d == 'U':
                if r > 0:
                    next_positions[(r - 1, c)].append(('U', r, c))
                else:
                    next_positions[(r, c)].append(('D', r, c))
            elif d == 'D':
                if r < n - 1:
                    next_positions[(r + 1, c)].append(('D', r, c))
                else:
                    next_positions[(r, c)].append(('U', r, c))
            elif d == 'R':
                if c < n - 1:
                    next_positions[(r, c + 1)].append(('R', r, c))
                else:
                    next_positions[(r, c)].append(('L', r, c))
            elif d == 'L':
                if c > 0:
                    next_positions[(r, c - 1)].append(('L', r, c))
                else:
                    next_positions[(r, c)].append(('R', r, c))

        # 충돌 처리: 하나만 있는 구슬만 남김
        beads = [
            (r, c, d[0])
            for (r, c), dirs in next_positions.items()
            if len(dirs) == 1
        ]

    print(len(beads))
