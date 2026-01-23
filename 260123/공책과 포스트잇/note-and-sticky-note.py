n, k, l = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse = True)

def check(h):
    h_cnt, l_cnt = 0, 0
    for i in range(h):
        if c[i] >= h:
            h_cnt += 1
        else:
            if h - c[i] > k or l_cnt + h - c[i] > k * l:
                break
            l_cnt += h - c[i]
            h_cnt += 1 
    if h_cnt >= h:
        return True
    else:
        return False

left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right) 