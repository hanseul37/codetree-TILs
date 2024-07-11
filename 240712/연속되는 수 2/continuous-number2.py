n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

cnt = 0
max = 0
for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        cnt = 1

print(max)