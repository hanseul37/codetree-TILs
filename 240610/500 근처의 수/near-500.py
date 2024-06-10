arr = list(map(int, input().split()))
a = []
b = []
for i in range(10):
    if arr[i] < 500:
        a.append(arr[i])
    else:
        b.append(arr[i])
print(max(a), min(b))