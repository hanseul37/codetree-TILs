arr = list(map(int, input().split()))
a = b = 0
for i in range(10):
    if i % 2 == 0:
        a += arr[i]
    else:
        b += arr[i]
if a > b:
    print(a-b)
else:
    print(b-a)