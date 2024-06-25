arr1 = input()
arr2 = input()
cnt = 0
for i in range(len(arr1) - 1):
    if arr1[i] == arr2[0] and arr1[i+1] == arr2[1]:
        cnt += 1
print(cnt)