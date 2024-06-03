arr = list()
ar = list(map(int, input().split()))
for i in range(10):
    if ar[i] != 0:
        arr.append(ar[i])
    else:
        break
ar = arr[::-1]
for i in range(len(ar)):
    print(ar[i], end=" ")