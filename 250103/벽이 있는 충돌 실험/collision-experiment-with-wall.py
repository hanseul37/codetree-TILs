from collections import Counter

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = []
    for _ in range(m):
        r, c, d = input().split()
        beads.append([int(r) - 1, int(c) - 1, d])
    for _ in range(2 * n):
        new_beads = [[-1, -1, ''] for _ in range(len(beads))]
        for i in range(len(beads)):
            if beads[i][2] == 'U':
                if beads[i][0] != 0:
                    new_beads[i] = [beads[i][0] - 1, beads[i][1], beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1], 'D']
            elif beads[i][2] == 'D':
                if beads[i][0] != n - 1:
                    new_beads[i] = [beads[i][0] + 1, beads[i][1], beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1], 'U']
            elif beads[i][2] == 'R':
                if beads[i][1] != n - 1:
                    new_beads[i] = [beads[i][0], beads[i][1] + 1, beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1], 'L']
            elif beads[i][2] == 'L':
                if beads[i][1] != 0:
                    new_beads[i] = [beads[i][0], beads[i][1] - 1, beads[i][2]]
                else:
                    new_beads[i] = [beads[i][0], beads[i][1], 'R']
            
        coord_counts = Counter((bead[0], bead[1]) for bead in new_beads)

        # 한 번만 등장한 좌표만 남김 (충돌하지 않은 구슬들)
        unique_beads = [bead for bead in new_beads if coord_counts[(bead[0], bead[1])] == 1]

        beads = unique_beads 
    print(len(beads))     

