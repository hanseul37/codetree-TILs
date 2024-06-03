arr = list(map(int, input().split()))
sum = 0
cnt = 0
for i in arr:
    if i == 0:
        break
    elif i % 2 == 0:
        cnt += 1
        sum += i
print(cnt, end=" ")
print(sum)