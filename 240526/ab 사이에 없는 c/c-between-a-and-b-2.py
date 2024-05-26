arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
ans = False
for i in range(a, b+1):
    if i % c == 0:
        ans = True
        break
if ans == True:
    print('NO')
else:
    print('YES')