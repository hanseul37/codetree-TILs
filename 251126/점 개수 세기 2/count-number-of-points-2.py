import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    try:
        # n: 점의 수, q: 쿼리의 수
        n_str, q_str = input().split()
        if not n_str or not q_str: return
        n, q = int(n_str), int(q_str)
    except (IOError, ValueError):
        return

    points = []
    all_x = []
    all_y = []

    # 점 좌표 입력
    for _ in range(n):
        try:
            x, y = map(int, input().split())
            points.append((x, y))
            all_x.append(x)
            all_y.append(y)
        except (IOError, ValueError):
            continue

    # 쿼리 좌표 입력
    queries = []
    for _ in range(q):
        try:
            x1, y1, x2, y2 = map(int, input().split())
            queries.append((x1, y1, x2, y2))
            all_x.append(x1)
            all_x.append(x2)
            all_y.append(y1)
            all_y.append(y2)
        except (IOError, ValueError):
            continue

    # 좌표 압축
    unique_x = sorted(list(set(all_x)))
    unique_y = sorted(list(set(all_y)))
    
    x_map = {coord: i for i, coord in enumerate(unique_x)}
    y_map = {coord: i for i, coord in enumerate(unique_y)}
    
    rows = len(unique_y)
    cols = len(unique_x)
    
    if rows == 0 or cols == 0:
        for _ in range(len(queries)):
            print(0)
        return

    # 2D 그리드에 점 개수 기록
    grid = [[0] * cols for _ in range(rows)]
    for x, y in points:
        if x in x_map and y in y_map:
            xi = x_map[x]
            yi = y_map[y]
            grid[yi][xi] += 1
            
    # 2D 누적 합 배열 생성 (계산 편의를 위해 1-based 인덱싱)
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows):
        for j in range(cols):
            prefix_sum[i+1][j+1] = grid[i][j] + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]

    # 쿼리 처리
    for x1, y1, x2, y2 in queries:
        _x1, _x2 = min(x1, x2), max(x1, x2)
        _y1, _y2 = min(y1, y2), max(y1, y2)

        # 쿼리 좌표가 압축된 좌표 맵에 없는 경우 처리
        if _x1 not in x_map or _x2 not in x_map or _y1 not in y_map or _y2 not in y_map:
            print(0)
            continue

        c1_idx = x_map[_x1]
        c2_idx = x_map[_x2]
        r1_idx = y_map[_y1]
        r2_idx = y_map[_y2]

        # 누적 합 배열을 사용하여 사각형 영역 내의 점 개수 계산
        ans = prefix_sum[r2_idx + 1][c2_idx + 1] \
            - prefix_sum[r1_idx][c2_idx + 1] \
            - prefix_sum[r2_idx + 1][c1_idx] \
            + prefix_sum[r1_idx][c1_idx]
            
        print(ans)

solve()
