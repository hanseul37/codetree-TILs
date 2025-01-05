t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = []
    for _ in range(m):
        r, c, d = input().split()
        beads.append([int(r) - 1, int(c) - 1, d])
    for _ in range(2 * n):
        new_beads = []
        position = [[0] * n for _ in range(n)]
        for i in range(len(beads)):
            if beads[i][2] == 'U':
                if beads[i][0] != 0:
                    new_beads.append([beads[i][0] - 1, beads[i][1], beads[i][2]])
                    position[beads[i][0] - 1][beads[i][1]] += 1
                else:
                    new_beads.append([beads[i][0], beads[i][1], 'D'])
                    position[beads[i][0]][beads[i][1]] += 1
            elif beads[i][2] == 'D':
                if beads[i][0] != n - 1:
                    new_beads.append([beads[i][0] + 1, beads[i][1], beads[i][2]])
                    position[beads[i][0] + 1][beads[i][1]] += 1
                else:
                    new_beads.append([beads[i][0], beads[i][1], 'U'])
                    position[beads[i][0]][beads[i][1]] += 1
            elif beads[i][2] == 'R':
                if beads[i][1] != n - 1:
                    new_beads.append([beads[i][0], beads[i][1] + 1, beads[i][2]])
                    position[beads[i][0]][beads[i][1] + 1] += 1
                else:
                    new_beads.append([beads[i][0], beads[i][1], 'L'])
                    position[beads[i][0]][beads[i][1]] += 1
            elif beads[i][2] == 'L':
                if beads[i][1] != 0:
                    new_beads.append([beads[i][0], beads[i][1] - 1, beads[i][2]])
                    position[beads[i][0]][beads[i][1] - 1] += 1
                else:
                    new_beads.append([beads[i][0], beads[i][1], 'R'])
                    position[beads[i][0]][beads[i][1]] += 1
            
        beads = [bead for bead in new_beads if position[bead[0]][bead[1]] == 1]

    print(len(beads))     

