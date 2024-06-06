arr = list(map(int, input().split()))
count = [0] * 6
for i in arr:
    count[i-1] += 1
for i in range(6):
    print(f'{i+1} - {count[i]}')