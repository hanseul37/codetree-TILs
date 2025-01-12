n, m, t = map(int, input().split())

r = []
c = []
d = []
w = []

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri) - 1)
    c.append(int(ci) - 1)
    d.append(di)
    w.append(int(wi))

for _ in range(t):
    arr = [[0] * n for _ in range(n)]
     
    for i in range(len(d)):
        if d[i] == 'U':
            if r[i] == 0:
                d[i] = 'D'
            else:
                r[i] -= 1
        elif d[i] == 'D':
            if r[i] == n - 1:
                d[i] = 'U'
            else:
                r[i] += 1
        elif d[i] == 'R':
            if c[i] == n - 1:
                d[i] = 'L'
            else:
                c[i] += 1
        elif d[i] == 'L':
            if c[i] == 0:
                d[i] = 'R'
            else:
                c[i] -= 1

        arr[r[i]][c[i]] += 1

    to_remove = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:  
                colli = []
                for l in range(len(d)):
                    if r[l] == i and c[l] == j:
                        colli.append((l, w[l])) 
                colli = sorted(colli, key=lambda x: -x[0])
                w[colli[0][0]] = sum(bead[1] for bead in colli)
                for l in range(1, len(colli)):
                    to_remove.append(colli[l][0])

    r = [r[i] for i in range(len(r)) if i not in to_remove]
    c = [c[i] for i in range(len(c)) if i not in to_remove]
    d = [d[i] for i in range(len(d)) if i not in to_remove]
    w = [w[i] for i in range(len(w)) if i not in to_remove]

print(len(d), max(w))