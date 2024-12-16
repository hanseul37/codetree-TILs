n, m, k = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

def apply_gravity(grid):
    """각 열의 숫자를 중력에 따라 아래로 내리는 함수"""
    for col in range(len(grid)):
        non_zero = [grid[row][col] for row in range(len(grid)) if grid[row][col] != 0]
        for row in range(len(grid) - len(non_zero)):
            grid[row][col] = 0
        for row in range(len(non_zero)):
            grid[len(grid) - len(non_zero) + row][col] = non_zero[row]

def explode(grid):
    """M개 이상의 연속된 숫자를 찾고 폭발시키는 함수"""
    to_explode = set()
    for col in range(len(grid)):
        count = 1
        for row in range(1, len(grid)):
            if grid[row][col] == grid[row - 1][col] and grid[row][col] != 0:
                count += 1
            else:
                if count >= m:
                    for r in range(row - count, row):
                        to_explode.add((r, col))
                count = 1
        if count >= m:  # 마지막 연속 구간 처리
            for r in range(len(grid) - count, len(grid)):
                to_explode.add((r, col))
    
    for r, c in to_explode:
        grid[r][c] = 0
    return len(to_explode) > 0  # 폭발이 발생했는지 여부 반환

def rotate_clockwise(grid):
    """상자를 시계방향으로 90도 회전"""
    n = len(grid)
    return [[grid[n - 1 - col][row] for col in range(n)] for row in range(n)]

# K번 회전 및 폭발 과정 수행
for _ in range(k):
    while True:
        apply_gravity(box)
        if not explode(box):
            break
    box = rotate_clockwise(box)

# 남아 있는 폭탄 수 계산
result = sum(row.count(0) == 0 for row in box)
print(result)
