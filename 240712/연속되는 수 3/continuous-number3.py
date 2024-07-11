n = int(input())
arr = [] 
for i in range(n):
    num = int(input())
    arr.append(num)

cnt, max = 0, 0
for i in range(n):
    if i == 0 or arr[i] * arr[i - 1] > 0:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        cnt = 1

print(max)