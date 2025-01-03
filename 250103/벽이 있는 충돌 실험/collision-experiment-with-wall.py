t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = []
    for _ in range(m):
        r, c, d = input().split()
        beads.append([int(r) - 1, int(c) - 1, d])

    for _ in range(2 * n):
        new_beads = []
        positions = []  # 새로 이동한 위치를 저장
        to_remove = set()  # 충돌 위치 저장

        for bead in beads:
            r, c, d = bead
            if d == 'U':
                new_r, new_c, new_d = (r - 1, c, 'U') if r > 0 else (r, c, 'D')
            elif d == 'D':
                new_r, new_c, new_d = (r + 1, c, 'D') if r < n - 1 else (r, c, 'U')
            elif d == 'R':
                new_r, new_c, new_d = (r, c + 1, 'R') if c < n - 1 else (r, c, 'L')
            elif d == 'L':
                new_r, new_c, new_d = (r, c - 1, 'L') if c > 0 else (r, c, 'R')

            # 새로운 위치 추가 및 충돌 확인
            if [new_r, new_c] in positions:
                to_remove.add((new_r, new_c))
            else:
                positions.append([new_r, new_c])
                new_beads.append([new_r, new_c, new_d])

        # 충돌 위치 제거
        beads = [
            bead for bead in new_beads if (bead[0], bead[1]) not in to_remove
        ]

    print(len(beads))
