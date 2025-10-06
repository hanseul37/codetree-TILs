from sortedcontainers import SortedList, SortedDict

n, m = map(int, input().split())
arr = list(map(int, input().split()))

intervals = SortedList([[0, n]], key=lambda x: x[0])
lengths = SortedDict()
lengths[n - 0 + 1] = 1  # 처음 구간 길이

for x in arr:
    idx = intervals.bisect_left([x, 0]) - 1
    l, r = intervals[idx]
    intervals.pop(idx)

    # 기존 구간 길이 제거
    old_len = r - l + 1
    lengths[old_len] -= 1
    if lengths[old_len] == 0:
        del lengths[old_len]

    # 새 구간들 생성
    new_intervals = []
    if l < x:
        new_intervals.append([l, x - 1])
    if x < r:
        new_intervals.append([x + 1, r])

    # 추가
    for nl, nr in new_intervals:
        intervals.add([nl, nr])
        new_len = nr - nl + 1
        lengths[new_len] = lengths.get(new_len, 0) + 1

    # 현재 최댓값 출력
    print(lengths.peekitem(-1)[0])
