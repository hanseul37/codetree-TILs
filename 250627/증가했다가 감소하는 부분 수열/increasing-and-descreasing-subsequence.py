n = int(input())
arr = list(map(int, input().split()))
up1, up2, down1, down2 = [1] * n, [1] * n, [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            up1[i] = max(up1[i], up1[j] + 1)
        elif arr[i] < arr[j]:
            down1[i] = max(down1[i], down1[j] + 1)
        
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            up2[i] = max(up2[i], up2[j] + 1)
        elif arr[i] > arr[j]:
            down2[i] = max(down2[i], down2[j] + 1)
        
max_length = max(max(up1), max(down1))
for i in range(n):
    max_length = max(max_length, up1[i] + down2[i] - 1)
    #max_length = max(max_length, down1[i] + up2[i] - 1)
print(max_length)



