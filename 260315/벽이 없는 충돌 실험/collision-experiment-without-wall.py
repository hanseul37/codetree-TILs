t = int(input())
for _ in range(t):
    n = int(input())
    x, y, w, d = [], [], [], []
    for i in range(n):
        xi, yi, wi, di = input().split()
        x.append((int(xi) + 1000) * 2)
        y.append((-int(yi) + 1000) * 2)
        w.append(int(wi))
        d.append(di)

    cnt, last_collision = 0, -1
    while len(d) > 1 and cnt <= 4000:
        cnt += 1
        pos = {}
        for i in range(len(d)):
            original_x, original_y = x[i], y[i]
            if d[i] == 'U' and y[i] != 0:
                y[i] -= 1
            elif d[i] == 'D' and y[i] != 4000:
                y[i] += 1
            elif d[i] == 'R' and x[i] != 4000:
                x[i] += 1
            elif d[i] == 'L' and x[i] != 0:
                x[i] -= 1      
            if original_x != x[i] or original_y != y[i]:
                moved = True

            key = (x[i], y[i])
            if key not in pos:
                pos[key] = []
            pos[key].append(i)

        if not moved:
            break

        beads, flag = [], False
        for b in pos.values():
            if len(b) == 1:
                beads.append(b[0])
            else:
                b.sort(key=lambda idx: [w[idx], idx], reverse=True)
                beads.append(b[0])
                flag = True
        if flag:
            last_collision = cnt
        beads.sort()

        x = [x[i] for i in beads]
        y = [y[i] for i in beads]
        w = [w[i] for i in beads]
        d = [d[i] for i in beads]

    print(last_collision)