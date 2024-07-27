arr = list(map(int, input().split()))
diff = 2000
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if k == i or k == j:
                continue
            for l in range(5):
                if l == i or l == j or l == k:
                    continue
                    
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