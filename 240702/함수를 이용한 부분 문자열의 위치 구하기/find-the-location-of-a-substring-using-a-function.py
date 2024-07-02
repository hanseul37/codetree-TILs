def location(arr1, arr2):
    index = -1
    for i in range(len(arr1) - len(arr2) + 1):
        flag = 0
        if arr1[i] == arr2[0]:
            for j in range(1, len(arr2)):
                if arr1[i+j] != arr2[j]:
                    flag = 1
                    break
            if flag != 1:
                index = i
                break
    return index

arr1 = input()
arr2 = input()
if location(arr1, arr2) == -1:
    print(-1)
else:
    print(location(arr1, arr2))