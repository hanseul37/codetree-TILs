t = int(input())

for _ in range(t):
    n = int(input())
    x, y, w, d = [], [], [], []

    for i in range(n):
        xi, yi, wi, di = input().split()
        x.append((int(xi) + 1000) * 2)
        y.append((-1 * int(yi) + 1000) * 2)
        w.append(int(wi))
        d.append(di)

    cnt = 0
    while len(d) > 1:
        if cnt > 4000 and len(d) == n:
            cnt = -1
            break

        position_map = {}
        for i in range(len(d)):
            if d[i] == 'U':
                y[i] -= 1
            elif d[i] == 'D':
                y[i] += 1
            elif d[i] == 'R':
                x[i] += 1
            elif d[i] == 'L':
                x[i] -= 1

            if x[i] < 0 or x[i] > 4000 or y[i] < 0 or y[i] > 4000:
                to_remove.add(i)
                continue

            pos = (x[i], y[i])
            if pos in position_map:
                position_map[pos].append(i)
            else:
                position_map[pos] = [i]

        to_remove = set()
        for pos, indices in position_map.items():
            if len(indices) > 1:
                indices.sort(key=lambda idx: (w[idx], idx), reverse=True)
                to_remove.update(indices[1:])

        x = [x[i] for i in range(len(x)) if i not in to_remove]
        y = [y[i] for i in range(len(y)) if i not in to_remove]
        w = [w[i] for i in range(len(w)) if i not in to_remove]
        d = [d[i] for i in range(len(d)) if i not in to_remove]
        cnt += 1
    print(cnt)