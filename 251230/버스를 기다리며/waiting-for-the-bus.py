n, m, c = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

def check(wait):
    bus_cnt, first_wait, person_in_bus = 0, -wait - 1, 0
    for person in t:
        if person_in_bus == c or person - first_wait > wait:
            bus_cnt += 1
            first_wait = person
            person_in_bus = 1
        else:
            person_in_bus += 1
        if bus_cnt > m:
            return False
    return True

left, right = 0, 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)