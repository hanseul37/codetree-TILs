n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri) - 1)
    c.append(int(ci) - 1)
    d.append(di)
    v.append(int(vi))

for _ in range(t):
    arr = [[0] * n for _ in range(n)]
    for i in range(len(v)):
        for j in range(v[i]):
            if d[i] == 'U':
                if r[i] == 0:
                    d[i] = 'D'
                    r[i] += 1
                else:
                    r[i] -= 1
            elif d[i] == 'D':
                if r[i] == n - 1:
                    d[i] = 'U'
                    r[i] -= 1
                else:
                    r[i] += 1
            elif d[i] == 'R':
                if c[i] == n - 1:
                    d[i] = 'L'
                    c[i] -= 1
                else:
                    c[i] += 1
            elif d[i] == 'L':
                if c[i] == 0:
                    d[i] = 'R'
                    c[i] += 1
                else:
                    c[i] -= 1
        arr[r[i]][c[i]] += 1

    to_remove = set() 
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k:  
                colli = []
                for l in range(len(v)):
                    if r[l] == i and c[l] == j:
                        colli.append((l, v[l])) 
                colli = sorted(colli, key=lambda x: x[1], reverse=True)
                for l in range(k, len(colli)):
                    to_remove.add(colli[l][0])

    r = [r[i] for i in range(len(r)) if i not in to_remove]
    c = [c[i] for i in range(len(c)) if i not in to_remove]
    d = [d[i] for i in range(len(d)) if i not in to_remove]
    v = [v[i] for i in range(len(v)) if i not in to_remove]  

print(len(v))
                
                