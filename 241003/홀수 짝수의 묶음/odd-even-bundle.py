n = int(input())
arr = list(map(int, input().split()))

odd, even = 0, 0
for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

max_cnt = 0
if even > odd:
    max_cnt = odd * 2 + 1
elif even < odd:
    change = 0
    while even + change < odd - 2 * change:
        change += 1
    if even + change == odd - 2 * change:
        max_cnt = 2 * (even + change)
    else:
        max_cnt = 2 * min(even + change, odd - 2 * change) + 1
else:
    max_cnt = 2 * even

print(max_cnt)