t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = [input().split() for _ in range(m)]
    for i in range(m):
        beads[i] = [int(beads[i][0]) - 1, int(beads[i][1]) - 1, beads[i][2]]
    for _ in range(2 * n):
        new_beads = [[-1, -1, ''] for _ in range(len(beads))]
        for i in range(len(beads)):
            if beads[i][2] == 'U':
                if beads[i][0] != 0:
                    new_beads[i] = [beads[i][0] - 1, beads[i][1], beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0] + 1, beads[i][1], 'D']
            elif beads[i][2] == 'D':
                if beads[i][0] != n - 1:
                    new_beads[i] = [beads[i][0] + 1, beads[i][1], beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0] - 1, beads[i][1], 'U']
            elif beads[i][2] == 'R':
                if beads[i][1] != n - 1:
                    new_beads[i] = [beads[i][0], beads[i][1] + 1, beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1] - 1, 'L']
            elif beads[i][2] == 'L':
                if beads[i][1] != 0:
                    new_beads[i] = [beads[i][0], beads[i][1] - 1, beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1] + 1, 'R']
            
        unique_beads = []
        visited = set()  
        for bead in new_beads:
            coord = (bead[0], bead[1])
            if coord in visited:
                unique_beads = [b for b in unique_beads if (b[0], b[1]) != coord]
            else:
                visited.add(coord)
                unique_beads.append(bead)
        beads = unique_beads  
    print(len(beads))     

