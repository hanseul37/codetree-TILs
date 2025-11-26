import sys

class FenwickTree:
    """ 펜윅 트리 (이진 인덱스 트리) """
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def add(self, i, delta):
        """ i번 인덱스에 delta 값을 더함 (0-based index) """
        i += 1  # 1-based로 변환
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        """ 0부터 i번 인덱스까지의 누적 합을 구함 (0-based index) """
        i += 1  # 1-based로 변환
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query_range(self, i, j):
        """ i부터 j번 인덱스까지의 구간 합을 구함 (0-based indices) """
        if i > j:
            return 0
        res = self.query(j)
        if i > 0:
            res -= self.query(i - 1)
        return res

def solve():
    """ 스윕 라인 알고리즘으로 문제 해결 """
    input = sys.stdin.readline
    try:
        line = input()
        if not line.strip(): return
        n, q = map(int, line.split())
    except (IOError, ValueError):
        return

    points = []
    all_y = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
        all_y.append(y)
    
    queries = []
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        queries.append((x1, y1, x2, y2, i))
        all_y.append(y1)
        all_y.append(y2)
    
    if not all_y:
        for _ in range(q):
            print(0)
        return

    # Y좌표 압축
    unique_y = sorted(list(set(all_y)))
    y_map = {coord: i for i, coord in enumerate(unique_y)}
    m = len(unique_y)
    
    events = []
    # 이벤트 타입: 0=쿼리 시작, 1=점, 2=쿼리 끝 (정렬 순서에 중요)
    
    for x, y in points:
        events.append((x, 1, y_map[y]))
            
    for x1, y1, x2, y2, i in queries:
        _x1, _x2 = min(x1, x2), max(x1, x2)
        _y1, _y2 = min(y1, y2), max(y1, y2)
        
        y1_idx = y_map[_y1]
        y2_idx = y_map[_y2]
        
        events.append((_x1, 0, y1_idx, y2_idx, i))
        events.append((_x2, 2, y1_idx, y2_idx, i))
    
    events.sort()
    
    answers = [0] * q
    bit = FenwickTree(m)
    
    for event in events:
        x, type = event[0], event[1]
        
        if type == 1:  # 점 이벤트
            _, _, y_idx = event
            bit.add(y_idx, 1)
        elif type == 0:  # 쿼리 시작 이벤트
            _, _, y1_idx, y2_idx, q_idx = event
            answers[q_idx] -= bit.query_range(y1_idx, y2_idx)
        else:  # 쿼리 끝 이벤트
            _, _, y1_idx, y2_idx, q_idx = event
            answers[q_idx] += bit.query_range(y1_idx, y2_idx)

    for ans in answers:
        print(ans)

solve()
