arr = list(map(int, input().split()))
digit = arr[0] + arr[1]
cnt = 0
for elem in str(digit):
    if elem == '1':
        cnt += 1
print(cnt)