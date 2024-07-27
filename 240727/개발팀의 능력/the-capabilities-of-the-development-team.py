arr = list(map(int, input().split()))
diff = 2000
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            for l in range(k + 1, 5):
                ability = [0] * 3
                ability[0] = arr[i] + arr[j]
                ability[1] = arr[k] + arr[l]
                ability[2] = sum(arr) - ability[0] - ability[1]
                ability.sort()
                if ability[0] != ability[1] and ability[0] != ability[2] and ability[1] != ability[2]:
                    if ability[2] - ability[0] < diff:
                        diff = ability[2] - ability[0]

if diff == 2000:
    print(-1)
else:
    print(diff)