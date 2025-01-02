t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    beads = [input().split() for _ in range(m)]
    for i in range(m):
        beads[i] = [int(beads[i][0]) - 1, int(beads[i][1]) - 1, beads[i][2]]
    for _ in range(2 * n):
        grid = {}  # 격자 기반 위치 기록
        next_beads = []  # 다음 단계 구슬 정보

        for x, y, d in beads:
            if d == 'U':
                nx, ny, nd = (x - 1, y, 'D') if x == 0 else (x - 1, y, d)
            elif d == 'D':
                nx, ny, nd = (x + 1, y, 'U') if x == n - 1 else (x + 1, y, d)
            elif d == 'L':
                nx, ny, nd = (x, y - 1, 'R') if y == 0 else (x, y - 1, d)
            elif d == 'R':
                nx, ny, nd = (x, y + 1, 'L') if y == n - 1 else (x, y + 1, d)

            if (nx, ny) in grid:
                grid[(nx, ny)] = None  # 충돌 발생
            else:
                grid[(nx, ny)] = (nx, ny, nd)

        # 충돌되지 않은 구슬만 다음 단계로 이동
        next_beads = [info for info in grid.values() if info is not None]
        beads = next_beads

    print(len(beads))
