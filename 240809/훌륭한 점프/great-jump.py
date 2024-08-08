n, k = map(int, input().split())
arr = list(map(int, input().split()))

point = 0
values = arr[0]
current_min = arr[0]

while point < n - 1:
    # 최대 k만큼 전진하면서 최소값 갱신
    for i in range(point + 1, min(point + k + 1, n)):
        if arr[i] < current_min:
            current_min = arr[i]
            point = i

    # 현재 최소값과 비교하여 최대값 갱신
    values = max(values, current_min)
    
    # 목적지 도달하면 루프 종료
    if point + k >= n - 1:
        values = max(values, min(arr[point + 1:]))
        break

print(values)