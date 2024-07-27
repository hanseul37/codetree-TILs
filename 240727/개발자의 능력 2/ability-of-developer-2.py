arr = list(map(int, input().split()))
min_diff = 2000000
total = sum(arr)
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            for l in range(k + 1, 6):
                ability = [0] * 3

                ability[0] = arr[i] + arr[j]
                ability[1] = arr[k] + arr[l]
                ability[2] = total - ability[0] - ability[1]
                ability.sort()
                min_diff = min(min_diff, ability[2] - ability[0])

                ability[0] = arr[i] + arr[k]
                ability[1] = arr[j] + arr[l]
                ability[2] = total - ability[0] - ability[1] 
                ability.sort()
                min_diff = min(min_diff, ability[2] - ability[0])

                ability[0] = arr[i] + arr[l]
                ability[1] = arr[j] + arr[k]
                ability[2] = total - ability[0] - ability[1]
                ability.sort()
                min_diff = min(min_diff, ability[2] - ability[0])

print(min_diff)