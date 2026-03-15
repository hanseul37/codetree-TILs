t = int(input())

for _ in range(t):
    n = int(input())

    x, y, w, d = [], [], [], []
    alive = [True] * n

    for i in range(n):
        xi, yi, wi, di = input().split()
        x.append((int(xi) + 1000) * 2)
        y.append((-int(yi) + 1000) * 2)
        w.append(int(wi))
        d.append(di)

    last_collision = -1

    for time in range(1, 4001):

        pos = {}

        for i in range(n):
            if not alive[i]:
                continue

            if d[i] == 'U':
                y[i] -= 1
            elif d[i] == 'D':
                y[i] += 1
            elif d[i] == 'L':
                x[i] -= 1
            else:
                x[i] += 1

            key = (x[i], y[i])
            pos.setdefault(key, []).append(i)

        collision = False

        for arr in pos.values():
            if len(arr) > 1:
                collision = True
                arr.sort(key=lambda i: (w[i], i), reverse=True)
                winner = arr[0]

                for i in arr[1:]:
                    alive[i] = False

        if collision:
            last_collision = time

    print(last_collision)