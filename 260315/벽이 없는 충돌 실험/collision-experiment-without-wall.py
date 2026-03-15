import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    atoms = []
    for i in range(n):
        x, y, w, d = input().split()
        x = (int(x) + 1000) * 2
        y = (int(y) + 1000) * 2
        w = int(w)

        if d == 'U':
            dx, dy = 0, 1
        elif d == 'D':
            dx, dy = 0, -1
        elif d == 'L':
            dx, dy = -1, 0
        else:
            dx, dy = 1, 0

        atoms.append([x, y, w, dx, dy, True])

    last = -1

    for t in range(1, 4001):

        pos = {}

        for i in range(n):
            if not atoms[i][5]:
                continue

            atoms[i][0] += atoms[i][3]
            atoms[i][1] += atoms[i][4]

            x, y = atoms[i][0], atoms[i][1]

            if not (0 <= x <= 4000 and 0 <= y <= 4000):
                atoms[i][5] = False
                continue

            pos.setdefault((x, y), []).append(i)

        collision = False

        for v in pos.values():
            if len(v) > 1:
                collision = True
                v.sort(key=lambda i: (atoms[i][2], i), reverse=True)

                winner = v[0]
                for i in v[1:]:
                    atoms[i][5] = False

        if collision:
            last = t

    print(last)