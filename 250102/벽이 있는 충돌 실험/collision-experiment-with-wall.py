t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = [input() for _ in range(m)]
    for i in range(m):
        beads[i][0] = int(beads[i][0]) - 1
        beads[i][1] = int(beads[i][1]) - 1
    for _ in range(2 * n):
        new_beads = [[-1, -1, ''] * len(beads)]
        for i in range(len(beads)):
            if beads[i][2] == 'U':
                if beads[i][0] != 0:
                    new_beads[i] = [beads[i][0] - 1, beads[i][1], beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0] + 1, beads[i][1], 'D']
            elif beads[i][2] == 'D':
            elif beads[i][2] == 'R':
            elif beads[i][2] == 'L':
            
        for i in range(len(new_beads)):
            

