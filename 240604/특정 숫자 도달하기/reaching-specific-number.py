arr = list(map(int, input().split()))
sum = 0
cnt = 0
for i in arr:
    if i < 250:
        sum += i
        cnt += 1
    else:
        break
print(sum, end=" ")
print(f'{sum/cnt:.1f}')