from sortedcontainers import SortedList

n = int(input())
arr = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    # x1과 x2 중 작은 값을 시작점으로 통일
    start_x, end_x = min(x1, x2), max(x1, x2)
    arr.append([start_x, y, i, 1])
    arr.append([end_x, y, i, -1])

# x좌표 기준으로 정렬, x가 같으면 v가 -1인 끝점이 먼저 오도록
arr.sort()

# cnt 대신 set을 사용하여 고유한 선분 ID를 저장
seen_as_lowest = set()
color = SortedList()

# 기존 for문 구조를 유지하면서 내부 로직 수정
for x, y, idx, v in arr:
    # 1. 변경 전 최하단 선분 확인
    lowest_before = color[0][1] if len(color) > 0 else -1

    # 2. 이벤트 처리 (선분 추가 또는 제거)
    if v == 1:
        color.add((y, idx))
    else:
        color.remove((y, idx))

    # 3. 변경 후 최하단 선분 확인
    lowest_after = color[0][1] if len(color) > 0 else -1

    # 4. 최하단 선분이 유효한 값으로 변경되었으면 set에 추가
    if lowest_after != lowest_before and lowest_after != -1:
        seen_as_lowest.add(lowest_after)

print(len(seen_as_lowest))

