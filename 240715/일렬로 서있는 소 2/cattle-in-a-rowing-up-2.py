n = int(input())
cows = list(map(int, input().split()))
cnt = 0
for i in range(len(cows) - 2):
    for j in range(i + 1, len(cows) - 1):
        for k in range(j + 1, len(cows)):
            if cows[i] <= cows[j] <= cows[k]:
                cnt += 1
print(cnt)